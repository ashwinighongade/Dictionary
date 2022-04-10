# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 
dict=  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
dict1={}
for x in dict:
    # for i in x:
    
    l=x.replace(' ','')
    dict1.update({x:dict[x]})
print(dict1)


