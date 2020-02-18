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
