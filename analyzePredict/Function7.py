def stop_words_remover(df):

    splitter = df['Tweets'].apply(lambda x: x.lower().split())
    df['Without Stop Words'] = splitter.apply(lambda x: [word for word in x if word not in stop_words_dict['stopwords']])
    return df
