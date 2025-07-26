# Authenticate
import requests
import time

# Replace with your actual Bearer Token (User OAuth 2.0 Access Token)
ACCESS_TOKEN = ''
USER_ID = '1718007556772085760'  # Get this from https://api.twitter.com/2/users/me

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# 1. Get your recent tweets (up to 100 at a time)
def get_my_tweets():
    url = f"https://api.twitter.com/2/users/{USER_ID}/tweets"
    params = {
        "max_results": 100,  # Max allowed
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json().get("data", [])

# 2. Delete a tweet by ID
def delete_tweet(tweet_id):
    url = f"https://api.twitter.com/2/tweets/{tweet_id}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 200:
        print(f"✅ Deleted tweet {tweet_id}")
    else:
        print(f"❌ Failed to delete {tweet_id}: {response.text}")

# 3. Loop and delete
def delete_all_my_tweets():
    tweets = get_my_tweets()
    print(f"Found {len(tweets)} tweets to delete.")
    for tweet in tweets:
        delete_tweet(tweet['id'])
        time.sleep(1)  # Avoid rate limits

if __name__ == '__main__':
    delete_all_my_tweets()
