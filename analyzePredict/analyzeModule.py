import numpy as np
import pandas as pd
def dictionary_of_metrics(items):
     dic = {}
     dic['mean'] = round(np.mean(items), 2)
     dic['median'] =round(np.median(items), 2)
     dic['var'] = round(np.var(items, ddof = 1),2)
     dic['std'] =round(np.std(items, ddof = 1), 2)
     dic['min'] = round(min(items), 2)
     dic['max'] =  round(max(items), 2)
     
     return dic 

def play_mod():
    print('module works')

### START FUNCTION
def word_splitter(df):
    df['Split Tweets'] = df['Tweets'].str.split(' ')
    return df
### END FUNCTION

