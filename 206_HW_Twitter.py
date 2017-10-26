import unittest
import tweepy
import requests
import json
import twitter_info
## SI 206 - HW
## COMMENT WITH:
## Your section day/time: Section 2 Wednesday 6-7pm
## Any names of people you worked with on this assignment: None


## Write code that uses the tweepy library to search for tweets with three different phrases of the 
## user's choice (should use the Python input function), and prints out the Tweet text and the 
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least 
## 1 blank line in between each of them, e.g.


## You should cache all of the data from this exercise in a file, and submit the cache file 
## along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets 
## about "rock climbing", when we run your code, the code should use CACHED data, and should not 
## need to make any new request to the Twitter API.  But if, for instance, you have never 
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles" 
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will 
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing



## **** For extra credit, create another file called twitter_info.py that 
## contains your consumer_key, consumer_secret, access_token, and access_token_secret, 
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information 
## for an 'extra' Twitter account you make just for this class, and not your personal 
## account, because it's not ideal to share your authentication information for a real 
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these 
## with variables rather than filling in the empty strings if you choose to do the secure way 
## for EC points
#loading the auth. info from another file
consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way
#initialize the tweepy api access
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) 

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except 
## 		statement shown in class.
def load_chahe(search_term):
    #try to open the cache, might fail if not exist
    try:
        cache=json.loads(open('{}'.format(search_term),'r').read())
        cache_status='S'
        print("cache found")
    except:
    #if not exist, use an empty dictionary as the cache
        cache={}
        cache_status='F'
    #return the status of cache and the cache
    return (cache_status,cache)
## 2. Write a function to get twitter data that works with the caching pattern, 
## 		so it either gets new data or caches data, depending upon what the input 
##		to search for is.
def search (search_term):
    #try to load cache file
    rtr=load_chahe(search_term)
    cache_status=rtr[0]
    cache=rtr[1]
    if cache_status=='F':#no cahe loaded commence searching
        searched_tweets = api.search(q=search_term, rpp=5, count=5)
        cache=searched_tweets
        open('{}'.format(search_term),'w').write(json.dumps(searched_tweets))#saves the cache with the search term as the file name
    else:#cahce loaded
        pass# do hnothing
    return cache#return the loaded cache

## 3. Using a loop, invoke your function, save the return value in a variable, and explore the 
##		data you got back!

i=0
got_pack=[]
while i < 3:
    search_term=input("please enter a term to search \n")
    print("fetching")
    got=search(search_term)#run search function, save returned cache file as got
    i+=1
## 4. With what you learn from the data -- e.g. how exactly to find the 
##		text of each tweet in the big nested structure -- write code to print out 
## 		content from 5 tweets, as shown in the linked example.
    for j in got['statuses']: #stucture is within the got dictionary;s statuses key, there are a list of differtent twittes
        print ("TEXT: {}".format(j['text']))
        print("CREATED AT: {}".format(j['created_at']))
        print("\n")






