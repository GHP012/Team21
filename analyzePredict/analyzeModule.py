def play_mod():
    print('module works')

# function 1
def dictionary_of_metrics(items):
    # your code here
    return {'mean':round(np.mean(items), 2), 'median':round(np.median(items), 2), 'std': round(np.std(items, ddof=1), 2), 'var':round(np.var(items, ddof=1), 2), 'min':round(min(items), 2), 'max': round(max(items), 2)}

#function 2
def five_num_summary(items):
    # your code here
    return {'max':round(max(items), 2), 'median':round(np.median(), 2), 'min': round(min(items), 2), 'q1': round(np.quantile(items, 0.25), 2), 'q3': round(np.quantile(items), 2)}

#function3
def date_parser(dates):
    # your code here
    return [date[:10] for date in dates]

#function4
def extract_municipality_hashtags(df):
    # your code here
    atlist_col = df['Tweets'].apply(lambda x: [word for word in x.split() if word[0]=='@'])
    hashtag_list_col = df['Tweets'].apply(lambda x: [word.lower() for word in x.split() if word[0]=='#']) # for some reason they want it in lowercase
    
    def checkat(lst):
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
            
    df['municipality']= atlist_col.apply(checkat)
    df['hashtags'] = hashtag_list_col.apply(lambda x: np.nan if x==[] else x)
    
    return df

#function5
def number_of_tweets_per_day(df):
    # your code here
    df = pd.to_datetime(df['Date'], yearfirst=True).apply(lambda x: x.date()).value_counts().to_frame()
    df = df.rename(columns={'Date':'Tweets'})
    df.index.name = 'Date'
    df.sort_index(inplace=True)
    return df

#function6
def word_splitter(df):
    # your code here
    df['Split Tweets'] = df['Tweets'].apply(lambda x: x.lower().split())
    return df

#function7
def stop_words_remover(df):
    # your code here
    splitwords = df['Tweets'].apply(lambda x: x.lower().split())
    df['Without Stop Words'] = splitwords.apply(lambda x: [word for word in x if word not in stop_words_dict['stopwords']])
    return df