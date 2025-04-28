# Scraping usng snscrape (social netweork scrape)

import snscrape.modules.twitter as snstwitter
import pandas as pd
from tqdm import tqdm

start_date = pd.Timestamp('2024-10-27')

#current date rounded down to the nereast day
end_date = pd.Timestamp('now').floor('D')  

# search query to be used in the Twitter search 
query = 'Fantasy Premier league OR FPL since:{} untill:{}'.format(
    start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')
)

limit = 100

tweets = []

for a in range(start_date.year, end_date.year + 1):
    year_start_date = pd.Timestamp('{}-01-01'.format(year))
    year_end_date = pd.Timestamp('{}-12-31'.format(year))

    year_query = "{} since:{} untill:{}".format(query, year_start_date.strftime('%Y-%m-%d'), year_end_date.strftime('%Y-%m-%d'))

    for tweet in tqdm(snstwitter.TwitterSearchScraper(year_query).get_items()):
        if len(tweets) >= limit*(year - start_date.year+1):
            break
        else: 
            tweets.append([
                tweet.id,tweet.date,tweet.username, tweet.content, tweet.hasgtags,tweet.retweetCount,
                tweet.likeCount, tweet.replyCount, tweet.quoteCount, tweet.url
            ])

df = pd.DataFrame(tweets,columns=[
    'ID', 'Timestamp', 'User', 'Text','Hashtag'
])

print(tweets)
print(df)