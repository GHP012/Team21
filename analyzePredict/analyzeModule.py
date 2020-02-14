def date_parser(list_dates):
  # [date[:10] for date in list_dates]
    new_list = []
    for date in list_dates:
        
        new_list.append(date[:10])
        
    return new_list
