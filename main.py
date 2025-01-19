from tweepy.client import Client
from utils.x_api import authenticate_x_api, search_recent_tweets

import os
import pandas as pd
from typing import Any, Dict, List


def save_tweets_to_files(
    tweets: List[Dict[str, Any]], output_dir: str = "data/tweets"
) -> None:
    """Save tweets to multiple file formats."""
    os.makedirs(name=output_dir, exist_ok=True)
    df: pd.DataFrame = pd.DataFrame(data=tweets)

    # Save to .TXT format
    df.to_csv(
        path_or_buf=os.path.join(output_dir, "tweets.txt"),
        sep="\t",
        index=False,
    )

    # Save to .JSON format
    df.to_json(
        path_or_buf=os.path.join(output_dir, "tweets.json"),
        orient="records",
        force_ascii=False,
    )

    # Save to .CSV format
    df.to_csv(
        path_or_buf=os.path.join(output_dir, "tweets.csv"),
        index=False,
        encoding="utf-8-sig",
    )

    # Save to .XLSX format
    df.to_excel(
        excel_writer=os.path.join(output_dir, "tweets.xlsx"),
        index=False,
    )


def main() -> None:
    """Main function to fetch and save tweets."""
    try:
        # Authenticate with the X API v2
        client: Client = authenticate_x_api()
    except Exception as error:
        print(f"Authentication failed: {error}")
        return

    query: str = "#แสตมป์อภิวัชร์"
    tweets: List[Dict[str, Any]] = []  # initialize an empty list for tweets

    try:
        # Fetch tweets
        tweets = search_recent_tweets(
            client=client,
            query=query,
            max_tweets=10,
        )
    except Exception as error:
        print(f"An error occurred while fetching tweets: {error}")
        return

    if tweets:
        print(f"Successfully fetched {len(tweets)} tweets.")
    else:
        print("No tweets were fetched.")
        return

    try:
        # Save tweets to files
        save_tweets_to_files(tweets=tweets)
        print("Tweets saved successfully.")
    except Exception as error:
        print(f"An error occurred while saving tweets: {error}")


if __name__ == "__main__":
    main()
