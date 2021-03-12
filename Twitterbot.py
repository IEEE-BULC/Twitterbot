import tweepy
consumer_key ='consumer key here'
consumer_secret = 'consumer secret key here'

key = 'consumer key'
secret= 'secret key '

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
