


# list1=[11,12,13,14,15,16]
# list2=[]
# i=0
# while i<len(list1):
#     if len(list1)

# dict1={'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}

# list1=[]
# for i in dict1:
#     list1.append(i['age'])
# print(list1)

dict1={'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
dict2={}
for i in dict1:
    dict2.update({i:dict1[i]['age']})
print(dict2)
    # print(dict1[i]['age'])

# dict1={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# list1=[]

# value = int(input("Enter the value :"))
# for i in dict1:
#     if dict1[i]==value:
#         list1.append(i)
# print(list1)


# list1=['a', 'b', 'c', 'd', 'e', 'f']
# list2=[1, 2, 3, 4, 5]
# dict1={}
# for i in range(len(list2)):
#     dict1.update({list1[i]:list2[i]})
# print(dict1)

# dict1={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# list1=[]
# for i in dict1:
#     b=(i,dict1[i])
#     # list1.append(b)
#     # b=(dict1[i])
#     list1.append(b)
# print(list1)




