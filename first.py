import tweepy
from tweepy import OAuthHandler
import imghdr

consumer_key = '1850167768051752960Lmagar4207'
consumer_secret = 'Lmagar4207'
access_token = '1850167768051752960-Lmagar4207'
access_token_secret = 'Lmagar4207'

auth = OAuthHandler(consumer_Key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print('first.py')