import numpy as np
import pandas as pd

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

#Function1
def dictionary_of_metrics(items):
    """ Function that calculates the mean, median, variance, standard deviation, minimum and maximum of list in items.

       Parameters:
         items(list): takes up a list of numbers.

       Returns:
         dictionary: returning the 'mean', 'median', 'var','std','min' , 'max',
         corresponding to the mean, median, variance, standard deviation, minimum and maximum of the input list.

       Examples:
         >>>dictionary_of_metrics(gauteng)
         {'mean': 26244.42, median': 24403.5, 'var': 108160153.17, 'std': 10400.01, 'min': 8842.0,'max': 39660.0}
    """
    dic = {}
    dic['mean'] = round(np.mean(items), 2)
    dic['median'] =round(np.median(items), 2)
    dic['var'] = round(np.var(items, ddof = 1),2)
    dic['std'] =round(np.std(items, ddof = 1), 2)
    dic['min'] = round(min(items), 2)
    dic['max'] =  round(max(items), 2)

    return dic

#Function2
def five_num_summary(items):
    '''Function takes a list of integers or floats & returns a dictionary of the five number summary.

       Parameters:
         items (list): List of integers or floats

       Returns:
         summary_dict (dict): dictionary of the five number summary of list elements

       Example:
       -----------
         >>> five_num_summary([111,2221,528,588,524])
         {'max': 2221.0,
             'median': 528.0,
             'min': 111.0,
             'q1': 524.0,
             'q3': 588.0}
    '''

    summary_dict = {}
    summary = np.quantile(items,[1, 0.5, 0, 0.25, 0.75])
    list1 = ["max","median","min","q1","q3"]
    for i in range(len(list1)):
        summary_dict[list1[i]] = summary[i]

    return summary_dict

 #Function3
def date_parser(dates):
    """
    Function 3: Date Parser
    Date Parser function that takes a list of datetime strings and returns only the
    date in 'yyyy-mm-dd' format.
    The function returns the date only from a list of items.
    The input is a list of datetime strings and it outputs a list of dates.
    The dates variable is a list of dates represented as strings.
    The string contains the date in 'yyyy-mm-dd' format and the time in hh:mm:ss foramt.
    The first three entries in this variable are:
    dates[:3] == [
        '2019-11-29 12:50:54',
        '2019-11-29 12:46:53',
        '2019-11-29 12:46:10'
        ]
    Function Specifications:
    The function should take a list of strings as input.
    Each string in the input list is formatted as 'yyyy-mm-dd hh:mm:ss'.
    The function should return a list of strings where each element in the returned
    list contains only the date in the 'yyyy-mm-dd' format.
    Arg:
    A list of datetime strings
    Return:
    A date or list of dates
    Examples:
    Input
    [ '2019-11-29 12:50:54' , '2019-11-29 12:46:53' , '2019-11-29 12:46:10']
    Output
    [ '2019-11-29' , '2019-11-29' , '2019-11-29' ]
    """

    result = []                       # Define an empty list
    for i in range(len(dates)):
        res = dates[i][:10]           # Accessing first 10 elements of string
        result.append(res)           # Inserts the new results into a list
    return result

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

#Function 6
def word_splitter(df):
    """ Splits sentences in a dataframe's column and returns a list of the separated words in lowercase

    Parameters:
    -----------

        df (dataframe): Dataframe of sentences in string format

    Returns:
    -----------

        (list): List of the seperated words in lowercase

     Examples
    -----------

    >>> word_splitter(df)
    @BongaDlulane Please send an email to mediades = [@bongadlulane, please, send, an, email to, mediades]

    """
    df['Split Tweets'] = list(map(lambda i: i.lower().split(),df.Tweets))
    return df

#Function7
def stop_words_remover(df):
    ''' Function counts removes english stop words from a tweet.

    parameter
    ---------
      df(DataFrame): pandas dataframe as input containing Twitter information

    returns
    -------
      (DataFrame): df DataFrame with additional column called 'Without Stop Words'. The column contains 
                   tokenised Tweets without stop-words and tokenized tweet is then added to column within
                   a list. 
    
    Example
    -------
    >>> twitter_feed = pd.DataFrame({'Tweets':['Cremora above the fridge', 'We'er almost done', 'Good work guys'],
                             'Date': ['2019-11-29 12:17:43', '2019-11-28 13:34:41', '2020-02-19 07:00:00']})
    >>> stop_words_remover(twitter_feed)
    
               
                         Tweets                  Date  Without Stop Words
    0  Cremora above the fridge   2019-11-29 12:17:43 	[cremora, fridge]  
    1         We'er almost done   2019-11-28 13:34:41             [we'er]
    2            Good work guys	  2020-02-19 07:00:00  [good, work, guys]

    '''

    splitter = df['Tweets'].apply(lambda x: x.lower().split())
    df['Without Stop Words'] = splitter.apply(lambda x: [word for word in x if word not in stop_words_dict['stopwords']])

    return df
