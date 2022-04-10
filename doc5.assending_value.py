# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
dict1={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
list1 =[]
for i in dict1:
    list1.append(dict1[i])
i = 0
while i < len(list1):
    j = 0
    while j < len(list1):
        if list1[i]>list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
        j+=1
    i+=1
print(list1)
dict2 = {}
for i in list1:
    for k in dict1 :
    # for j in list1:
        if dict1[k] == i:
            dict2.update({k:i})
print(dict2)    
            
# j = 0
# for k in dict1 :
#     for i in dict1:
#         if dict1[i] == list1[j]:
#             dict2[i] = dict1[i]
#     j+=1
# print(dict2)
    
        

       
            
        

            
