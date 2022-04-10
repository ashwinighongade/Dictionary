# Q37.Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
# key=[x,y,z]
dict={}
list1=[]
list2=[]
list3=[]
for i in range(11,41):
    if i<20:
        list1.append(i)
        dict.update({"x":list1})
    if i>20 and i<30:
        list2.append(i)
        dict.update({"y":list2})
    if i>30 and i<40:
        list3.append(i)
        dict.update({"z":list3})
print(dict)
for i in dict:
    for j in dict[i]:
        if j%5==0:
            print(j)
        