#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
#argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '2tuZK2YZgR01mTIQAmVEqxl2p'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'JjDoXlGcp3DNH24P02VUdIyrHSiYzKxTnbKqNHBxBinkJfeVlv'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '16504071-cEhpsGfg7YKS1Zq8cckxeVzvI1HW00zOZrQOeZV8I'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'xe0lZfTFresyGX0NmNioqHbm6DwCGAYXckGyhzu8QaoFg'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
 
#loadcache

#dictionaryvalues a = {key: 'value', key: 'value'}
meTwitter = api.me()
print meTwitter

#define seed accounts
#check cache 
#	If cache is older than a month or cache file isn't there
#		if nocache; collect 1 yr worth of tweets and save as cache file
#		if cacheold; collect 1 month worth of tweets and add it to cache file

#Source Dictionary definition
#source = {'key 0': {'result': resultWeightAsInt}, 'key 1': {'result': resultWeightAsInt}}
#as the name would suggest, the keys should be unique

#dict = {'a': {'a': [1]},'b': [0,1,2]}
#a = AutoVivification() <-- Look in to that more closlier
#dict['a']['a'].append(3) #IS PERFECTLY VALID PYTHON
#dict['b'].append(3)
#print dict


#Iterate through text
#	starting at index 0, 
#	choose key value length based on predetermined Order length (order-2 looks at two characters for each key, etc etc)
#		check for key value in source dictionary
#			if true: add result to source dictionary
#			if false: add key value and result to source dictionary
#		add str.len() of key value to index

