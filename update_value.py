# 51. A Python Dictionary contains List as value. Write a Python program to update the list values in the said dictionary. Go to the editor
# Original Dictionary:
# {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}

dict1={'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
dict2={}
for i in dict1:
    list1=[]
    if i=='Math':
        for j in dict1['Math']:
            add=j+2
            list1.append(add)
            dict2.update({'Math':list1})
    list2=[]
    if i=='Physics':
        for j in dict1['Physics']:
            sub=j-2
            list2.append(sub)
            dict2.update({'Physics':list2})
    list3=[]
    if i=='Chemistry':
        # list3.append(dict1[i])
        dict2.update({'Chemistry':dict1[i]})
print(dict2)

