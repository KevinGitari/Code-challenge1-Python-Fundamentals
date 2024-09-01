#Sort list of tuples

def sort_by_age(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

tuples_list = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
sorted_list = sort_by_age(tuples_list)
print(sorted_list)  
