def word_splitter(df):
    '''Function splits the sentences in a dataframe's column into a list of the separate words.
       The created lists are placed in a new column named 'Split Tweets' in the original dataframe.

       Parameters:
           df (dataframe): list of separate words

       Returns:
          pd.Dataframe: dataframe with additoanl columns

       '''
    df['Split Tweets'] = df['Tweets'].str.split(' ')
    return df
