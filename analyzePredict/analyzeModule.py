import numpy as np
import pandas as pd

def play_mod():
  print('module works')
 
#Function1
def dictionary_of_metrics(items):
    `""" Function that calculates the mean, median, variance, standard deviation, minimum and maximum of list in items.

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
