dict={"value1":5, "value2":4, "value3":3, "value4":2, "value5":1}
key=input("entet the key which delete :")
dict1={}
for i in dict:
    if i != key:
        dict1.update({i:dict[i]})
print(dict1)

# if key in dict:
#     del dict[key]
# print(dict)
