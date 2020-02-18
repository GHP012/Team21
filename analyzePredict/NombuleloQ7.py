### START FUNCTION
def stop_words_remover(df):
    """ Splits sentences in a dataframe's column and returns a list of the separated words in lowercase without stop words
    
    Parameters:
    -----------

        df (dataframe): Dataframe of sentences in string format

    Returns:
    -----------

        (list): List of the seperated words in lowercase withouth stop words

     Examples
    -----------

    @BongaDlulane Please send an email to mediades = ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za']
    
    """
    
    split_tweets = list(map(lambda i: i.lower().split(),df.Tweets))
    stop_words_list = stop_words_dict['stopwords']
    df['Without Stop Words'] = list(map(lambda i: list(filter(lambda word: word not in stop_words_list,i)),split_tweets))
    return df

### END FUNCTION