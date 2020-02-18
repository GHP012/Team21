def play_mod():
    print('module works')
### START FUNCTION
def word_splitter(df):
    """ Splits sentences in a dataframe's column and returns a list of the separated words           in lowercase
    
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
### END FUNCTION