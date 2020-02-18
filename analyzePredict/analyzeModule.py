import numpy as np
import pandas as pd
def dictionary_of_metrics(items):

""" Function that calculates the mean, median, variance, standard deviation, minimum and maximum of list in items.

    Parameters:
    items(list): takes up a list of numbers.

    Returns:
    dictionary: returning the 'mean', 'median', 'var','std','min' , 'max',
    corresponding to the mean, median, variance, standard deviation, minimum and maximum of the input list.

    Examples:
    >>>dictionary_of_metrics(gauteng)
   {'mean': 26244.42,median': 24403.5, 'var': 108160153.17, 'std': 10400.01, 'min': 8842.0,'max': 39660.0}
   
    
"""
     dic = {}
     dic['mean'] = round(np.mean(items), 2)
     dic['median'] =round(np.median(items), 2)
     dic['var'] = round(np.var(items, ddof = 1),2)
     dic['std'] =round(np.std(items, ddof = 1), 2)
     dic['min'] = round(min(items), 2)
     dic['max'] =  round(max(items), 2)
     
     return dic 

