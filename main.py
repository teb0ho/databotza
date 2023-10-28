from tasks import kaizer_chiefs_days
import requests
from requests_oauthlib import OAuth1
import os
import logging

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_KEY_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('databotza.log', 'w', 'utf-8')
handler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(message)s', '%Y-%m-%d %H:%M:%S'))
root_logger.addHandler(handler)


kaizer = kaizer_chiefs_days.KaizerChiefsDays()


def connect_to_oauth(consumer_key1, consumer_secret1, access_token1, access_token_secret1):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key1, consumer_secret1, access_token1, access_token_secret1)
    return url, auth


def format_fact(text):
    return {"text": "{}".format(text)}


def main():
    text = kaizer.execute()
    payload = format_fact(text)
    url, auth = connect_to_oauth(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    request = requests.post(
        auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
    )
    logging.info(text)
    logging.info(request.text)
    logging.info('finished')


if __name__ == "__main__":
    main()
