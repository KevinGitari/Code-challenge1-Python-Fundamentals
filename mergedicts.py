#Merge dictionaries

def merge_dicts(dict1, dict2):
   
    result = {}
    
    
    for key, value in dict1.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
            
    
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    
    return result

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merged = merge_dicts(dict1, dict2)
print(merged)

