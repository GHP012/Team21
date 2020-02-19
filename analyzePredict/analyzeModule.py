import numpy as np
import pandas as pd

def play_mod():
    print('module works')

#function4
def extract_municipality_hashtags(df):
    '''pandas dataframe and returns a modified dataframe that includes two new
    columns that contain information about the municipality and hashtag of the tweet.

    parameter
    ---------
      df(DataFrame): pandas dataframe as input containing Twitter information

    returns
    -------
      (DataFrame): pandas dataframe similar to inputed df but with 2 appended columns
                   (named 'municipality' and 'hashtags'). The 2 columns contain identified
                   major metro municipality and hashtags of tweets, respectively. The
                   columns will contain np.nan entries where municipality or hashtags are
                   not found.

    Example
    -------
      >>> twitter_feed = pd.DataFrame({'Tweets':['#ESKOMFREESTATE #MEDIASTATEMENT: ESKOM PLANS ELECTRICITY SUPPLY INTERRUPTIONS',
                                       'RT @CityPowerJhb: #RandburgOutage power outage in Greater Randburg'],
                             'Date': ['2019-11-29 12:17:43', '2019-11-28 13:34:41']})
      >>> extract_municipality_hashtags(twitter_feed)

                                       Tweets                 Date   unicipality                            hashtags
      0    #ESKOMFREESTATE #MEDIASTATEMENT...  2019-11-29 12:17:43  NaN           [#eskomfreestate, #mediastatement]
      1  RT @CityPowerJhb: #RandburgOutage...  2019-11-28 13:34:41  Johannesburg                   [#randburgoutage]

    '''

    def checkat(lst):
        '''
        This function checks if all the @-mentions are included in dictionary of major metros
        and returns the identified metro.
        The function is used with ".apply" method to isolate major metro in @-mentions
        '''
        mun_present = False
        if lst == []:
            return np.nan
        else:
            for at in lst:
                for key in mun_dict.keys():
                    if key in at:
                        mun_present = True
                        return mun_dict[key]
            if not mun_present:
                return np.nan


    #create pandas.Series objects containing list of columns with all @-mentions and hashtags, respectively
    atlist_col = df['Tweets'].apply(lambda x: [word for word in x.split() if word[0]=='@'])
    hashtag_list_col = df['Tweets'].apply(lambda x: [word.lower() for word in x.split() if word[0]=='#'])


    df['municipality']= atlist_col.apply(checkat)
    df['hashtags'] = hashtag_list_col.apply(lambda x: np.nan if x==[] else x)

    return df

#function5
def number_of_tweets_per_day(df):
    ''' Function which counts the number of tweets that were posted per day

    parameter
    ---------
      df(DataFrame): pandas dataframe as input containing Twitter information

    returns
    -------
      (DataFrame): New dataframe, grouped by day, with the number of tweets for that day. The dataframe is
                   indexed by Date which tweets were, and the column named 'Tweets' which corresponds
                   number of tweets.

    Example
    -------
    >>> twitter_feed = pd.DataFrame({'Tweets':['#ESKOMFREESTATE...', 'RT @CityPowerJhb...', 'Guys load..'],
                             'Date': ['2019-11-29 12:17:43', '2019-11-28 13:34:41', '2020-02-19 07:00:00']})
    >>> number_of_tweets_per_day(twitter_feed)

                Tweets
          Date
    2019-11-29       2
    2020-02-19       1
    '''
    
    df = pd.to_datetime(df['Date'], yearfirst=True).apply(lambda x: x.date()).value_counts().to_frame()
    df = df.rename(columns={'Date':'Tweets'})
    df.index.name = 'Date'
    df.sort_index(inplace=True)
    return df
