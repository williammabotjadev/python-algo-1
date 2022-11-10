# setdefault operation example

def usual_dict(dict_data):
    new_data = {}
    for k, v in dict_data:
        if k in new_data:
            new_data[k].append(v)
        else:
            new_data[k] = [v]
    return new_data 

def setdefault_dict(dict_data):
    new_data = {}
    for k, v in dict_data:
        new_data.setdefault(k, []).append(v)
    return new_data

