import os
import asyncio
import re
from dotenv import load_dotenv
from methods.utils import fetch_website_contents
from openai import AsyncOpenAI

# ── Environment setup ─────────────────────────────────────────────────────────

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("⚠️  No OPENAI_API_KEY found. Please set it in your .env file.")

openAI = AsyncOpenAI()

# ── Prompts ───────────────────────────────────────────────────────────────────

system_prompt = """
You are a helpful assistant that analyzes the contents of a website,
and provides a good summary with all the metadata presented clearly, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""

# ── Helpers ───────────────────────────────────────────────────────────────────

def is_valid_url(url: str) -> bool:
    """
    Basic URL validation:
    - Must start with http:// or https://
    - Must have a non-empty domain with at least one dot
    """
    pattern = re.compile(
        r'^https?://'                  # http:// or https://
        r'(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}'  # domain (e.g. example.com)
        r'(?:[/?#]\S*)?$',             # optional path / query / fragment
        re.IGNORECASE,
    )
    return bool(pattern.match(url.strip()))


def messages_for(website: dict) -> list:
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + str(website)},
    ]


async def summarize(url: str) -> str:
    website = await fetch_website_contents(url)
    if not website:
        return "❌ Could not fetch website content. Please check the URL and try again."

    response = await openAI.chat.completions.create(
        model="gpt-5-nano",
        messages=messages_for(website),
    )
    return response.choices[0].message.content


def print_summary(summary: str) -> None:
    """Print the markdown summary with a visual separator."""
    separator = "─" * 60
    print(f"\n{separator}")
    print(summary)
    print(f"{separator}\n")


# ── Main loop ─────────────────────────────────────────────────────────────────

async def main():
    print("=" * 60)
    print("       🌐  Website Summarizer")
    print("=" * 60)
    print("""Enter a URL to summarize, or type 'exit' to quit.\n
note: there is a character limit of 5000 characters for the website content, so very long articles may be truncated.\n""")

    while True:
        raw_input = input("🔗 Enter URL: ").strip()

        # Exit condition
        if raw_input.lower() == "exit":
            print("\n👋 Goodbye!")
            break

        # Empty input
        if not raw_input:
            print("⚠️  No URL entered. Please try again.\n")
            continue

        # URL validation
        if not is_valid_url(raw_input):
            print(
                "⚠️  Invalid URL. Make sure it starts with http:// or https:// "
                "and contains a valid domain (e.g. https://example.com).\n"
            )
            continue

        # Fetch & summarise
        print()
        summary = await summarize(raw_input)
        print_summary(summary)

        # Prompt to continue or exit
        next_action = input("Type 'exit' to quit, or press Enter to summarize another URL: ").strip()
        if next_action.lower() == "exit":
            print("\n👋 Goodbye!")
            break

        print()


if __name__ == "__main__":
    asyncio.run(main())