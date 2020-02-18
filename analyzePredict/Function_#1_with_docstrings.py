def dictionary_of_metrics(items):
    '''Function to calculate mean, median, variance, standard deviation, minimum and maximum of a list of items.

        Parameters:
            items (list): list of floats or integers

        Returns:
            new_dict (dict): dictionary of mean, median, variance, standard deviation, minimum and maximum list of items

        Examples:
        ----------
        >>>>>dictionary_of_metrics(gauteng)
        {'mean': 26244.42,
         'median': 24403.5,
         'var': 108160153.17,
         'std': 10400.01,
         'min': 8842.0,
         'max': 39660.0}
        '''

    new_dict= {'mean':   round(np.mean(items), 2),
               'median': round(np.median(items), 2),
               'var':    round(np.var(items, ddof=1), 2),
               'std':    round(np.std(items, ddof =1), 2),
               'min':    round(min(items), 2),
               'max':    round(max(items), 2)}


    return new_dict
