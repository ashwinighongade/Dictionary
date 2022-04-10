# 35. Write a Python program to count the number of items in a dictionary value that is a list.
# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# Sample output: 5
dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for i in dict:
    for j in dict[i]:
        count+=1
print(count)
# for y in dict.values():
#     if type(y)==list:
#         for i in y:
#             count+=1
# print(count)