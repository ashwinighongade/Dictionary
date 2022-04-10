dict1={1: "a", 3: "b", 4: "c", 2: "n", 0: "x"}

list1 =[]
for n,v in dict1.items():
    list1.append(n)
print(list1)
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
dict2 = {}
for i in range(len(list1)):
    for k in dict1 :
    # for j in list1:
        if k == i:
            dict2.update({i:dict1[k]})
print(dict2)
    