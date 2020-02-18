def date_parser(dates):
    '''Function that takes as input a list of the datetime strings and returns list with only the date in "yyyy-mm-dd" format.

       Parameters:
           dates (list): List of strings in "yyyy-mm-dd hh:mm:ss" format

       Returns:
           reformated date (list): list in "yyyy-mm-dd" format"

       Example:
       ---------
       >>> date_parser(['2019-11-29 12:50:54',
                        '2019-11-29 12:46:53',
                        '2019-11-29 12:46:10'
                       ])

       ['2019-11-29', '2019-11-29', '2019-11-29']
    '''
    return [date[:10] for date in dates]
