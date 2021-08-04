import numpy as np 
import pandas as pd 

from twython import Twython

from tqdm import *

tweet_ids = pd.read_csv('2015_nepal_eq_cf_labels.csv')

CONSUMER_KEY = 'RCbQCBsFvx0FElNqjPakrSq81'
CONSUMER_SECRET = '3wae9yVfDkTbYMpiE4zFTbxsHTnCnmQfatOxIHBgGOKND7ZLk0'

OAUTH_TOKEN = '2350532065-Q5Taf42USTbvFqjU769FkkGVCS6KykQYpRNDUv7'
OAUTH_SECRET = 'pZ1PU06bVSYXt6ykWqQCoDGyC6rdlM8BzsfjBh99o8uRi'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET)

test_id = tweet_ids.tweet_id[0][1:-1]

test_id = tweet_ids.tweet_id[1][1:-1] 
try: tweet = twitter.show_status(id=test_id); print(tweet['text']) 
except: print ("oh rats")

tweet_ids['tweet_texts'] = u''

for i in tqdm(range(2400, len(tweet_ids))):
    individual_id = tweet_ids.tweet_id.iloc[i][1:-1]
    try: tweet = twitter.show_status(id=individual_id)['text']
    except: tweet = None
    tweet_ids.set_value(i, 'tweet_texts', tweet)

tweet_ids.to_csv('csv1.csv', encoding = 'utf-8')

stripped_tweets = tweet_ids[pd.notnull(tweet_ids.tweet_texts)]

stripped_tweets.to_csv('csv2.csv', encoding = 'utf-8')


