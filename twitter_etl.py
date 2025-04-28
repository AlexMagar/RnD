import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

def run_twitter_etl():

    access_key = "qG6LN0rHD4tOyyZkzMYTWDlvp" 
    access_secret = "kKcWQQtkyaHew0KX2ZuJpOI6rthFIcighCq4DJpoXqIkj71Q3D" 
    consumer_key = "11850162293415518208-w6HHd7A0vuZLOqMxHVxy6COClE7FKN"
    consumer_secret = "8fFxMPDdTjh8KekiRv2AhMScAtEo7dIsKL1BBhvbRBSEd"

#     access_key = "qG6LN0rHD4tOyyZkzMYTWDlvp"
# access_secret = 'kKcWQQtkyaHew0KX2ZuJpOI6rthFIcighCq4DJpoXqIkj71Q3D'
# consumer_key = "11850162293415518208-w6HHd7A0vuZLOqMxHVxy6COClE7FKN"
# consumer_secret = "8fFxMPDdTjh8KekiRv2AhMScAtEo7dIsKL1BBhvbRBSEd"

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    # # # Creating an API object 
    api = tweepy.API(auth)
    print("sth")

    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        print("Error during authentication", e)

    # tweets = api.user_timeline(screen_name='@elonmusk', 
    #                         # 200 is the maximum allowed count
    #                         count=200,
    #                         include_rts = False,
    #                         # Necessary to keep full_text 
    #                         # otherwise only the first 140 words are extracted
    #                         tweet_mode = 'extended'
    #                         )

    # print("give me sth", tweets)
    # list = []
    # for tweet in tweets:
    #     text = tweet._json["full_text"]

    #     refined_tweet = {"user": tweet.user.screen_name,
    #                     'text' : text,
    #                     'favorite_count' : tweet.favorite_count,
    #                     'retweet_count' : tweet.retweet_count,
    #                     'created_at' : tweet.created_at}
        
    #     list.append(refined_tweet)

    # df = pd.DataFrame(list)
    # df.to_csv('refined_tweets.csv')

run_twitter_etl()