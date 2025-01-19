import tweepy

import os
import requests
from dotenv import load_dotenv
from typing import Any, Dict, List

# Load environemnt variables
load_dotenv()


def authenticate_x_api() -> tweepy.Client:
    """Authenticate with the X API v2."""
    return tweepy.Client(
        bearer_token=os.getenv(key="BEARER_TOKEN"),
        consumer_key=os.getenv(key="API_KEY"),
        consumer_secret=os.getenv(key="API_KEY_SECRET"),
        access_token=os.getenv(key="ACCESS_TOKEN"),
        access_token_secret=os.getenv(key="ACCESS_TOKEN_SECRET"),
    )


def search_recent_tweets(
    client: tweepy.Client, query: str, max_tweets: int
) -> List[Dict[str, Any]]:
    """Search for tweets containing a specific hashtag using X API v2."""
    all_tweets: List = []
    next_token = None

    while len(all_tweets) < max_tweets:
        try:
            response: Any | requests.models.Response | tweepy.client.Response
            response = client.search_recent_tweets(
                query=query,
                max_results=max_tweets,
                tweet_fields=["id", "text", "created_at", "public_metrics"],
                user_fields=["username"],
                next_token=next_token,
            )

            if not response.data:
                break

            all_tweets.extend(
                [
                    {
                        "id": tweet.id,
                        "created_at": tweet.created_at,
                        "text": tweet.text,
                        "user": tweet.author_id,
                        "retweets": tweet.public_metrics["retweet_count"],
                        "likes": tweet.public_metrics["like_count"],
                    }
                    for tweet in response.data
                ]
            )
            next_token: Any | Any = response.meta.get("next_token")
            if not next_token:
                break
        except tweepy.errors.TooManyRequests:
            print("Error: Rate limit exceeded.")
            break
        except Exception as error:
            print(f"An error occurred: {error}")
            break

    return all_tweets
