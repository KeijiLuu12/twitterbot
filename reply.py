import tweepy
import keys

def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_secret)

    return tweepy.API(auth)

def tweet_reply(tweet_api: tweepy.API, message: str, user_id: int):

    tweet_api.update_status(message, in_reply_to_status_id= user_id)

    print("Had an interaction today!")


if __name__ == '__main__':
    api = api()
    mentions = api.mentions_timeline()
    if mentions:
        user_id_response = mentions[0].id
        user_name = mentions[0].user.screen_name
        reply = "Wow! You have broken me out of the vicious cycle of a bot!\nNow back to the grind..."
        twitter_reply = '@' + user_name + '\n' + reply
        tweet_reply(api, twitter_reply, user_id_response)
