import snscrape.modules.twitter as sntwitter
import pandas as pd 

query = 'python'
tweets = []
limit = 50

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break
    else: 
        tweets.append([tweet.data, tweet.user.username, tweet.content])

print(tweets)
