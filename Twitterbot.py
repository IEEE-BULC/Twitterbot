import tweepy
consumer_key ='consumer key here'
consumer_secret = 'consumer secret key here'

key = 'consumer key'
secret= 'secret key '

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
api.update_status('Twitter bot reporing in live')
api = tweepy.API(auth)
tweets= API.mentions_timeline()
print(tweets[0].text)
