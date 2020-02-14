
    ### START FUNCTION
def five_num_summary(items):
    summary_dict = {}
    summary = np.quantile(items,[1, 0.5, 0, 0.25, 0.75])
    list1 = ["max","median","min","q1","q3"]
    for i in range(len(list1)):
        summary_dict[list1[i]] = summary[i]
                                 
    return summary_dict

### END FUNCTION