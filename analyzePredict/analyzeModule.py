def play_mod():
    print('module works')

### START FUNCTION
# Question 6 -rough draft
def word_splitter(df):
    df['Split Tweets'] = np.nan
    for index, row in df.iterrows():
        df['Split Tweets'][index] = row['Tweets'].split()
  
    return df




### START FUNCTION
def word_splitter(df):
    df['Split Tweets'] = df['Tweets'].str.split(' ')
    return df
### END FUNCTION