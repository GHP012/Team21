def date_parser(dates):
"""
Function 3: Date Parser

Date Parser function that takes a list of datetime strings and returns only the
date in 'yyyy-mm-dd' format.

The function returns the date only from a list of items.
The input is a list of datetime strings and it outputs a list of dates.

The dates variable is a list of dates represented as strings.
The string contains the date in 'yyyy-mm-dd' format and the time in hh:mm:ss foramt.
The first three entries in this variable are:
dates[:3] == [
    '2019-11-29 12:50:54',
    '2019-11-29 12:46:53',
    '2019-11-29 12:46:10'
    ]

Function Specifications:
The function should take a list of strings as input.
Each string in the input list is formatted as 'yyyy-mm-dd hh:mm:ss'.
The function should return a list of strings where each element in the returned
list contains only the date in the 'yyyy-mm-dd' format.

Arg:
A list of datetime strings

Return:
A date or list of dates

Examples:
Input
[ '2019-11-29 12:50:54' , '2019-11-29 12:46:53' , '2019-11-29 12:46:10']

Output
[ '2019-11-29' , '2019-11-29' , '2019-11-29' ]

"""

    strdate = []
    for i in range(len(dates)):
        strd = dates[i][:10]
        strdate.append(strd)
    return strdate
