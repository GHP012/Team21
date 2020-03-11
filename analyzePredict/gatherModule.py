
# General:
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For numerical computation
import json
import datetime #for date formatting
# For plotting and visualization:
from IPython.display import display
import pyodbc

def pull_tweets(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET, count=100):
    """
    Twitter scrapper function
    This function takes in tweets from specified Twitter account and returns a
    DataFrame with two columns.This script requires that 'selenium' and
    'pandas' be installed into the Python enviroment you are running.
    The columns consist of one where the date is shown and another with all the
    charaters in the tweet.
    The input is data taken directly from Twitter.
    The output is a column with the date as a string and another with the tweet
    as a string.
    
    NB! Function makes use of Chrome webdriver. User must ensure that correct 
    webdriver is included in working directory. 

        Parameters:
        ----------
        CONSUMER_KEY(str)
        CONSUMER_SECRET(str)
        ACCESS_TOKEN(str)
        ACCESS_SECRET(str)
        count(str)= number of tweets scraped from twitter

        Returns:
        --------
        DataFrame with two columns with the date and characters of tweets
        scrapped from twitter website

        Example of output:
        ------------------
        date                                   tweet
    1  2020-03-05 08:23:49   #Eskom #MediaStatement\n\nEskom to institute l...
    2  2020-03-05 08:22:00   #EskomExpoTurns40 Have YOU participated in Esk...
    3  ...
    4  ...
    """
   
    extractor = __twitter_setup(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    
    tweets = extractor.user_timeline(id = '@Eskom_SA' , count=100,
                                 include_rts=True)
    
    tweets_for_col = [tweet.text for tweet in tweets]
    dates_for_col = [tweet.created_at for tweet in tweets]
    
    tweets_df = pd.DataFrame()
    
    tweets_df['date'] = dates_for_col
    tweets_df['tweet'] =  tweets_for_col
  
    
    return tweets_df
   
def __twitter_setup(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET):
    """
    Utility function to setup the Twitter's API
    with access and consumer keys from Twitter.
    """

    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth, timeout=1000)
    return api
