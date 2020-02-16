def date_parser(dates):
"""
Extracts Date from a list containing datetime series

Arg:
list of datetimes

Return:
A date / list of dates

Examples:
Input
[ '2019-11-29 12:50:54' , '2019-11-29 12:46:53' , '2019-11-29 12:46:10']

Output
[ '2019-11-29' , '2019-11-29' , '2019-11-29' ]


"""



    result = []
    for i in range(len(dates)):
        res = dates[i][:10]
        result.append(res)
    return result
