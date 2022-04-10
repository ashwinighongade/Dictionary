# Q43.Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. 
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}



list1=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dict={}
for i in list1:
    
    if i[0] not in dict.keys():
        dict.update({i[0]:[i[1]]})
    else:
        list_temp=dict[i[0]]
        list_temp.append(i[1])
        dict.update({i[0]:list_temp})
        
print(dict)

