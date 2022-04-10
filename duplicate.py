# Write a program to remove duplicate keys.
dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# dict1={}
# for key,value in dic.items():
#     if value not in dict1.values():
#         dict1[key]=value
# print(dict1)

dict={}
for i in dic:
    for j in dic:
        if i!=j:
            dict.update({i:dic[i]})
print(dict)
