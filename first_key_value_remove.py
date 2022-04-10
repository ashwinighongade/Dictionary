# Write a program remove the first key value pair from a nested dictionary.
dic= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}

# del dic[3]["A"]
# print(dic)
dict1={}
dict={}
for i in dic:
    # print(dic[i])
    if i==3:
        for j in dic[3]:
            if j!='A':
                dict1.update({j:dic[3][j]})
            dict.update({i:dict1})
    else:
        dict.update({i:dic[i]})
print(dict1)
print(dict)


