import tweepy


api_key = "" # your api key
api_secret = "" # your api secret
bearer_token = r"" # your bearer token
access_token = "" # your access token
access_token_secret = "" # your access token secret

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):  
        api.retweet(tweet.id)
        api.create_favorite(tweet.id)
        print("Retweet successfull")


stream = MyStream(bearer_token)

rules = tweepy.StreamRule("(#python OR #django OR #flask OR #pip) (-is:retweet -is:reply)")
stream.add_rules(rules)

stream.filter()