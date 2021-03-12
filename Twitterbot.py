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
for tweet in tweets:
  if '#ieeebulc' in tweet.text.lower():
    print(str(tweet.id) + ' - ' + tweet.text)

def read_last_seen(FILE_BANE):
      file_read = open("FILE_NAME", 'r')
      last_seen_id = int(file_read().strip())
      file_read.close()
      return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id)
  file_write= open(FILE_NAME ,'w')
  file_write.writer(str(last_seen_id))
  file_write.close()
  return
  tweets = api.mentions_timeline() 
