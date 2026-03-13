import trafilatura
from trafilatura.settings import use_config
import requests

# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def fetch_website_contents(url, char_limit=5000):
    """
    Return the title and contents of the website at the given url;
    truncate to {char_limit} characters as a sensible limit
    """

    try:
        # 1. Handle Network Errors (Timeout or Connection Issues)
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status() # Raises an error for 4xx or 5xx responses
    except Exception as e:
        return False

    try:
        html = response.text
        # Extract metadata
        metadata = trafilatura.extract_metadata(html, default_url=url)

        # Extract main content
        config = use_config()
        config.set("DEFAULT", "EXTRACTION_TIMEOUT", "30")

        content = trafilatura.extract(
            html,
            output_format="txt",     # "txt" or "markdown"
            include_comments=False,
            include_tables=True,
            no_fallback=False,               # use fallback extractors if needed
            config=config,
        )
        text = content or ""

        # Apply char_limit — None means no limit
        if char_limit is not None:
            text = text[:char_limit]

        return {
            "url": url,
            "title": metadata.title if metadata else None,
            "author": metadata.author if metadata else None,
            "date": metadata.date if metadata else None,
            "text": text,
        }
    except Exception as e:
        return False



