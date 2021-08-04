import tweepy
consumer_key = "gDH0ByIWSnkwLoZLSIg0jRVFX"
consumer_secret = "XIVNQbChOT9lOTq8SS0NEaS3JPbxeet3C1M8yPqoUTL8FODGsh"
access_token = "2350532065-z7fVQb72iTpSZKfKNl4VlrPePkpdUswlHVQpiQX"
access_token_secret = "n4AMFOj3E7iqKQJz8QhIxhJwhSYTMDDhcNmRxmUnSO7Xc"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

#result=api.search(q='Kerala Floods',language='en')

#for x in result:
#	print(x.text)
maxTweets=10000
for tweet in tweepy.Cursor(api.search,q="Cyclone Titli -filter:retweets").items(maxTweets) :  
    if (not tweet.retweeted) and ('RT @' not in tweet.text):
    	print(tweet.text.encode("utf-8"))

