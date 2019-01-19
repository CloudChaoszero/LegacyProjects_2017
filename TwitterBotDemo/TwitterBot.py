import os

import tweepy
import json
import time

consumer_key = str(os.getenv("consumer_key"))
consumer_secret = str(os.getenv("consumer_secret"))
access_key = str(os.getenv("access_key") ) 
access_secret = str(os.getenv("access_secret"))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, parser = tweepy.parsers.JSONParser() )

api.update_status("Running #Heroku app using #Python : Test 3")