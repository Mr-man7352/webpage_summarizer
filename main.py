import os
from dotenv import load_dotenv
from methods.utils import fetch_website_contents
from IPython.display import Markdown, display
from openai import OpenAI

def main():
    content = fetch_website_contents("https://reactjs.org/", char_limit=5000)
    if not content:
        print("Failed to fetch website content.")
        return
    print(f"Title  : {content['title']}")
    print(f"Author : {content['author']}")
    print(f"Date   : {content['date']}")
    print("-" * 60)
    print(content["text"])


if __name__ == "__main__":
    main()
