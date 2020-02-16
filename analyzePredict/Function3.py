def date_parser(dates):

    result = []
    for i in range(len(dates)):
        res = dates[i][:10]
        result.append(res)
    return result
    
