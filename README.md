# Website Summarizer 🌐

A Python tool that fetches webpage content and generates concise, actionable summaries using OpenAI's API.

## Features

- **URL Fetching**: Automatically extracts content from any website using Playwright and BeautifulSoup
- **Smart Summarization**: Uses OpenAI's GPT API to generate intelligent summaries with metadata
- **URL Validation**: Built-in validation to ensure valid URLs before processing
- **Interactive CLI**: User-friendly command-line interface for easy interaction
- **Content Limits**: Respects 5000 character limits to avoid token overflow
- **News Detection**: Automatically identifies and summarizes news/announcements

## Requirements

- Python 3.13+
- OpenAI API key
- Chromium (for Playwright)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/webpage_summarizer.git
   cd webpage_summarizer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or if using uv/pip with pyproject.toml:
   ```bash
   pip install -e .
   ```

3. **Install Chromium for Playwright** (required for web scraping):
   ```bash
   playwright install chromium
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   Get your API key from [OpenAI's platform](https://platform.openai.com/api-keys)

## Usage

### Running the CLI

```bash
python main.py
```

The tool will prompt you to enter URLs. Example session:

```
============================================================
       🌐  Website Summarizer
============================================================
Enter a URL to summarize, or type 'exit' to quit.

note: there is a character limit of 5000 characters for the website content, so very long articles may be truncated.

🔗 Enter URL: https://example.com
[Summary will be displayed here]

🔗 Enter URL: exit
👋 Goodbye!
```

### Using with Jupyter Notebook

Open `main.ipynb` for notebook-based usage with examples and interactive exploration.

## How It Works

1. **URL Validation**: Validates that the input is a properly formatted URL
2. **Content Fetching**: Uses Playwright to load the webpage and BeautifulSoup to extract text
3. **Content Cleaning**: Filters out navigation elements and other non-essential text
4. **AI Summarization**: Sends content to OpenAI's API (limited to 5000 characters)
5. **Markdown Output**: Returns formatted summary with clear sections

## Project Structure

```
webpage_summarizer/
├── main.py              # Main CLI application
├── main.ipynb          # Jupyter notebook for interactive use
├── pyproject.toml      # Project metadata and dependencies
├── README.md           # This file
├── .env                # Environment variables (create this)
└── methods/
    └── utils.py        # Utility functions for web scraping
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

## Error Handling

The tool handles common issues gracefully:
- **Invalid URLs**: Rejected with pattern matching before processing
- **Fetch Failures**: Returns error message if website cannot be reached
- **API Issues**: Notifies user if OpenAI API key is missing or invalid

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository** and create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and test thoroughly:
   ```bash
   python main.py  # Test the CLI
   ```

3. **Write clear commit messages**:
   ```bash
   git commit -m "Add feature: descriptive message"
   ```

4. **Submit a Pull Request** with a description of your changes

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to new functions
- Test with real URLs before submitting

### Areas for Contribution

- [ ] Add support for PDF summarization
- [ ] Implement caching for repeated URLs
- [ ] Add language detection and multilingual support
- [ ] Improve content extraction accuracy
- [ ] Add export formats (JSON, CSV, PDF)
- [ ] Test coverage improvements

## Troubleshooting

**Issue**: `OPENAI_API_KEY not found`
- Solution: Create `.env` file with your OpenAI API key

**Issue**: `Playwright chromium not installed`
- Solution: Run `playwright install chromium`

**Issue**: `Invalid URL format`
- Ensure your URL starts with `http://` or `https://`

**Issue**: `Website content could not be fetched`
- Check if the website is accessible in your browser
- Some websites may block automated requests

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the code documentation

---

**Happy summarizing! 🚀**

