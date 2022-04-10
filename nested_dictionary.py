# Write a Python program to convert more than one list to nested dictionary. 
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim R
list1=['S001', 'S002', 'S003', 'S004']
list2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list3=[85, 98, 89, 92]
list5=[]


for i in range(len(list2)):
    dict1={}
    d2={}
    d2.update({list2[i]:list3[i]})
    dict1.update({list1[i]:d2})
    list5.append(dict1)
print(list5)
