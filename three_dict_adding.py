# Write a program such that the below given dictionaries are into a single dictionary and add the values having same key.
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# output={1:10,2:20,3:30,4:40,5:50,6:60}

dic1={1:10,2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}

for i in dic1:
    if i in dic2:
        # if i in dic3:
        dic2.update({i:dic1[i]+dic2[i]})
    else:
        dic2.update({i:dic1[i]})
for j in dic3:
    if j not in dic2:
        dic2.update({j:dic3[j]})
        
print(dic2)



# Write a Python script to concatenate the following dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={2:30, 4:40}
# dic3={2:50,6:60}

# for i in dic1:
#     if i in dic2:
#         if i in dic3:
#             dic2.update({i:dic1[i]+dic2[i]+dic3[i]})
#     else:
#         dic2.update({i:dic1[i]})
# for j in dic3:
#     if j not in dic2:
#         dic2.update({j:dic3[j]})
        
# print(dic2)

