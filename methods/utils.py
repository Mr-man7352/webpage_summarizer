import trafilatura
from trafilatura.settings import use_config
from playwright.async_api import async_playwright


# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

async def fetch_website_contents(url, char_limit=5000):
    """
    Return the title and contents of the website at the given url;
    truncate to {char_limit} characters as a sensible limit
    """

    try:
        # 1. Handle Network Errors (Timeout or Connection Issues)
        """Fetch for dynamic/JS-rendered sites."""
        print("This will take a moment... grab a coffee! ☕")
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)
            await page.wait_for_timeout(6000)  # Wait 6s for JS to render
            content = await page.content()
            await browser.close()
    except Exception as e:
        print(f"Error fetching website contents for {url}: {e}")
        return False

    try:
        html = content
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



