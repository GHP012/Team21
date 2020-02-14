import numpy as np

def five_num_summ(items):
    
    items = np.array(items)
    dic = {}
    dic['max'] = round(max(items), 2)
    dic['median'] = round(np.percentile(items, 50), 2)
    dic['min'] = round(min(items), 2)
    dic['q1'] = round(np.percentile(items, 25, interpolation = 'lower'), 2)
    dic['q3'] = round(np.percentile(items, 75, interpolation = 'lower'), 2)
                          
    return dic
