# Twitter Hashtag Scraper

This Python script fetches tweets containing a specific hashtag (e.g., `#แสตมป์อภิวัชร์`) using the **Twitter API v2** and saves the data in multiple formats (`.txt`, `.json`, `.csv`, `.xlsx`). It is designed for personal, educational, and non-commercial use.

---

## Features

- **Fetch Tweets** : Retrieve tweets containing a specific hashtag.
- **Multiple Formats** : Save tweet data in `.txt`, `.json`, `.csv`, and `.xlsx` formats.
- **Rate Limit Handling** : Automatically handles rate limits by waiting and retrying.
- **Error Handling** : Gracefully handles errors during tweet fetching and file saving.

---

## Prerequisites

Before running the script, ensure you have the following:

1. **Twitter Developer Account**:

   - Apply for a developer account at the [Twitter Developer Portal](https://developer.twitter.com/).
   - Create a project and app to obtain API credentials.

2. **API Credentials**:

   - `BEARER_TOKEN`
   - `API_KEY`
   - `API_KEY_SECRET`
   - `ACCESS_TOKEN`
   - `ACCESS_TOKEN_SECRET`

3. **Python 3.8+** : Ensure Python is installed on your system.

---

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/nanonymoussu/get_tweets_by_hashtag.git
   cd get_tweets_by_hashtag
   ```

2. **Create a Virtual Environment** :

   ```bash
   uv venv venv
   ```

3. **Activate the Virtual Environment** :

   - On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

   - On Windows:

   ```bash
   .\venv\Scripts\activate
   ```

4. **Install Dependencies** :

   ```bash
   uv pip install tweepy pandas openpyxl python-dotenv
   ```

5. **Set Up Environment Variables** :

   - Create a `.env` file in the root directory:

   ```env
   API_KEY=your_api_key_here
   API_KEY_SECRET=your_api_key_secret_here
   ACCESS_TOKEN=your_access_token_here
   ACCESS_TOKEN_SECRET=your_access_token_secret_here
   BEARER_TOKEN=your_bearer_token_here
   ```

   - Replace the placeholders with your actual Twitter API credentials.

---

## Usage

1. **Run the Script** :

   ```bash
   python main.py
   ```

2. **Output** :

   - The script will fetch up to **10 tweets** containing the specified hashtag (`#แสตมป์อภิวัชร์` by default).
   - The tweets will be saved in the `data/tweets/` directory in the following formats:
     - `tweets.txt`: Tab-separated text file.
     - `tweets.json`: JSON file.
     - `tweets.csv`: CSV file.
     - `tweets.xlsx`: Excel file.

3. **Customize the Hashtag** :

   - To fetch tweets for a different hashtag, modify the `query` variable in the `main.py` file:

   ```python
   query: str = "#your_hashtag_here"
   ```

---

## Error Handling

- **Rate Limit Exceeded** :
  - If the rate limit is exceeded, the script will wait for 15 minutes and retry.
  - If no tweets are fetched due to an error, the script will exit without saving files.
- **File Saving Errors** :
  - If an error occurs while saving files, the script will print an error message and exit.

---

## Project Structure

```bash
twitter-hashtag-scraper/
├── .env              # Environment variables (API keys, etc.)
├── main.py           # Main script to run the program
├── README.md         # Project documentation
├── requirements.txt  # Project dependencies
├── utils/            # Utility functions/modules
│   └── x_api.py      # Twitter API wrapper
└── data/             # Folder to store output files
    └── tweets/       # Folder for tweet data
```

---

## Dependencies

- **tweepy** : For interacting with the Twitter API.
- **pandas** : For data manipulation and saving files.
- **openpyxl** : For saving data in Excel format.
- **python-dotenv** : For managing environment variables.

---

## License

This project is licensed under the **MIT License** . See the [LICENSE](https://github.com/nanonymoussu/get_tweets_by_hashtag/blob/main/LICENSE) file for details.

---

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

---

## Acknowledgments

- [Twitter Developer Portal](https://developer.twitter.com/) for providing the API.
- [Tweepy Documentation](https://docs.tweepy.org/) for the Python library used to interact with the Twitter API.

---

## Contact

For questions or feedback, please contact:

- **E-mail** : [nanon2546@gmail.com](mailto:nanon2546@gmail.com)
- **GitHub** : [nanonymoussu](https://github.com/nanonymoussu)
