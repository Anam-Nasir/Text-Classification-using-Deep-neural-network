
from __future__ import division

import numpy as np 
import pandas as pd 

import spacy
from spacy.tokens.doc import Doc
import inspect

from textacy.vsm import Vectorizer
import textacy.vsm

import scipy.sparse as sp

from tqdm import *

import re

from pymprog import *

tweets = pd.read_csv('2015_nepal_eq_cf_labels.csv', encoding = 'ISO-8859-1')

tweets = tweets.dropna()


# removing URLS
tweets.tweet_text = tweets.tweet_text.apply(lambda x: re.sub(u'http\S+', u'', x))   

# removing @... 
tweets.tweet_text = tweets.tweet_text.apply(lambda x: re.sub(u'(\s)@\w+', u'', x))

# removing hashtags
tweets.tweet_text = tweets.tweet_text.apply(lambda x: re.sub(u'#', u'', x))

tweets.tweet_text = tweets.tweet_text.apply(lambda x: x.replace(u'RT', u''))

nlp = spacy.load('en')

spacy_tweets = []

for doc in nlp.pipe(tweets.tweet_text, n_threads = -1):
    spacy_tweets.append(doc)

main_words = [u'earthquake', u'killed', u'injured', u'stranded', u'wounded', u'hurt', u'helpless', u'wrecked', u'nepal']


useful_entities = [u'NORP', u'FACILITY', u'ORG', u'GPE', u'LOC', u'EVENT', u'DATE', u'TIME']

content_tweets = []
for single_tweet in tqdm(spacy_tweets):
    single_tweet_content = []
    for token in single_tweet: 
        if ((token.ent_type_ in useful_entities)  
            or (token.pos_ == u'NUM') 
            or (token.lower_ in main_words)):
            single_tweet_content.append(token)
    content_tweets.append(single_tweet_content)





vectorizer = Vectorizer(tf_type='linear', apply_idf=True, idf_type='smooth')


term_matrix = vectorizer.fit_transform([tok.lemma_ for tok in doc] for doc in spacy_tweets)

np_matrix = term_matrix.todense()

print(np_matrix.shape)

for key in sorted(vectorizer.vocabulary)[1000:1015]:
    print (key, vectorizer.vocabulary[key])


for token in content_tweets[500]:
    print (token.lemma_, vectorizer.vocabulary[token.lemma_], np.max(np_matrix[:,vectorizer.vocabulary[token.lemma_]]))

tfidf_dict = {}
content_vocab = []
for tweet in content_tweets: 
    for token in tweet: 
        if token.lemma_ not in tfidf_dict: 
            content_vocab.append(token.lemma_)
            tfidf_dict[token.lemma_] = np.max(np_matrix[:,vectorizer.vocabulary[token.lemma_]])


for key in sorted(tfidf_dict)[500:505]:
    print ("WORD:" + str(key) + " -- tf-idf SCORE:" +  str(tfidf_dict[key]))


begin('COWTS')

# Defining my first variable, x 
# This defines whether or not a tweet is selected
x = var('x', len(spacy_tweets), bool)

# Check this worked
x[1000]

# Also defining the second variable, which defines
# whether or not a content word is chosen
y = var('y', len(content_vocab), bool)


len(y), y[0]


maximize(sum(x) + sum([tfidf_dict[content_vocab[j]]*y[j] for j in range(len(y))]));

## Maximum length of the entire tweet summary

# Was 150 for the tweet summary, 
# But generated a 1000 word summary for CONABS
L = 1000

# hiding the output of this line since its a very long sum 
sum([x[i]*len(spacy_tweets[i]) for i in range(len(x))]) <= L;

def content_words(i):
    '''Given a tweet index i (for x[i]), this method will return the indices of the words in the 
    content_vocab[] array
    Note: these indices are the same as for the y variable
    '''
    tweet = spacy_tweets[i]
    content_indices = []
    
    for token in tweet:
        if token.lemma_ in content_vocab:
            content_indices.append(content_vocab.index(token.lemma_))
    return content_indices



def tweets_with_content_words(j):
    '''Given the index j of some content word (for content_vocab[j] or y[j])
    this method will return the indices of all tweets which contain this content word
    '''
    content_word = content_vocab[j]
    
    index_in_term_matrix = vectorizer.vocabulary[content_word]
    
    matrix_column = np_matrix[:, index_in_term_matrix]
    
    return np.nonzero(matrix_column)[0]

for j in range(len(y)):
    sum([x[i] for i in tweets_with_content_words(j)])>= y[j]

for i in range(len(x)):
    sum(y[j] for j in content_words(i)) >= len(content_words(i))*x[i]


solve()

result_x =  [value.primal for value in x]
result_y = [value.primal for value in y]

end()

chosen_tweets = np.nonzero(result_x)
chosen_words = np.nonzero(result_y)

len(chosen_tweets[0]), len(chosen_words[0])

for i in chosen_tweets[0]:
    print ('--------------')
    print (spacy_tweets[i])


random_tweets = np.random.choice(spacy_tweets, size=11)

for i in random_tweets:
    print ('--------')
    print (i)

cowts_tweets = []
for i in chosen_tweets[0]:
    cowts_tweets.append(spacy_tweets[i])

for tweet in cowts_tweets[:10]:
    print ('--------')
    print (tweet)


        
            
        
			
