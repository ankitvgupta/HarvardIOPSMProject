from __future__ import absolute_import, print_function
# think about taking out tweets that are links
# https://jsonformatter.curiousconcept.com/

import datetime
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy

# sentiment analysis import
# import indicoio

from bs4 import BeautifulSoup
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

# desired tag

# keys needed to access APIs
consumer_key = 'kzgnPvD38avA7fh73ZvOT9tLa'
consumer_secret = '64AWYxTJUFW3giAY67TGUzdNEVu41pvq8iSMKeBf3v7ow2EAWG'
access_token = "462550008-ND20bj81rJt4S98aNAP7SG3dLUNrwZoYyNu5yfKJ"
access_token_secret = "d9yqIYnfexULBviBu7KvWbpeoWXHb0XaPyHVb3nc67rXt"
# indicoio.config.api_key = '7eb077799570ac2dd7917d2fb7ad4d60'

# twitter authorization stuff...so unnecessary
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# define possible choices for sentiment
sentiment_choices = ['Negative', 'Neutral', 'Positive']

# initialize counts for each type of sentiment in a dictionary
sentiment_counts = {}
for sentiment in sentiment_choices:
	sentiment_counts[sentiment] = 0

# organize sentiments of posts by date
sentiment_trends = {}

# looks like POST statuses/filter is the best streaming API to use but lets start with normal api

# def make_api_request(url=None):
# 	"""Returns the dictionary from an API request."""
# 	# make an ajax get request
# 	request = urllib2.Request(url)
# 	f = urllib2.urlopen(request)
# 	response = f.read()
# 	f.close()

# 	# get and return desired data
# 	api_dict = json.loads(response)
# 	return api_dict

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data_string):
        data = json.loads(data_string.encode('utf-8'))
        print("text: ", data["text"])
        print("location: ", data["user"]["location"])
        print("description: ", data["user"]["description"])
        print("UTC offset: ", data["user"]["utc_offset"])
        print("time zone: ", data["user"]["time_zone"])
        print("geo enabled: ", data["user"]["geo_enabled"])
        print("geo: ", data["geo"])
        print("coordinates: ", data["coordinates"])
        print("place: ", data["place"])
        print("\n\n")
        return True

    def on_error(self, status):
        print(status)
        
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
stream.filter(track=["hillary"])

# # create csv of desired info for viewing in Excel
# img_data = open('img_data.csv', 'w')
# img_data.write("Creation date: %s UTC\n" % str(datetime.datetime.utcnow()))

# img_counter = 1
