dict1={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
list1 =[]
for i in dict1:
    list1.append(i)
i = 0
while i < len(list1):
    j = 0
    while j < len(list1):
        if list1[i] < list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
        j+=1
    i+=1
print(list1)
# dict2={list1[0],dict1[list1[0]]}
dict2 = {}
for i in range(len(list1)):
    for k in dict1 :
    # for j in list1:
        if k == list1[i]:
            dict2.update({list1[i]:dict1[k]})
print(dict2)    
            
# a={'4':5,'6':7,'1':3,'2':4}
# l=sorted(a.items())
# print(l)
# m={}
# for i in l:
#     m[i[0]]=i[1]
#     # m.update({i[0]:i[1]})
# print(m)