import json
import random
import tweepy
import keys

def get_info():
    with open('/Users/kiwi/coding/PythonCode/twitterbot/facts.json', 'r', encoding='utf-8') as read_file:
        facts = json.load(read_file)
    random_fact = random.choice(facts["facts"])
   
    return str(random_fact)

def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_secret)

    return tweepy.API(auth)

def tweet(tweet_api: tweepy.API, message: str, image_path=None):

    if image_path:
        tweet_api.update_status_with_media(message, image_path)
    else:
        tweet_api.update_status(message)

    print('Tweeted~')

def tweet_reply(tweet_api: tweepy.API, message: str, user_id: int):

    tweet_api.update_status(message, in_reply_to_status_id= user_id)

    print("Had an interaction today!")

if __name__ == '__main__':
    tweet_body = get_info()
    api = api()
    tweet(api, tweet_body, None)
