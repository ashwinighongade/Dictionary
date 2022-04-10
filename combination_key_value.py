# 58. Write a Python program to get all combinations of key-value pairs in a given dictionary. Go to the editor
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Combinations of key-value pairs of the said dictionary:
# [{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]}, {'VI': [1, 4, 12], 'VII': [1, 3, 8]}]
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5]}
# Combinations of key-value pairs of the said dictionary:
# [{'V': [1, 3, 5], 'VI': [1, 5]}]
dict1={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
dict2={}
list1=[]
i=0
l=len(dict1)
print(l)
res=[]
out_count=0
for i in dict1:
    if (out_count==l-1):
        break
    in_count=0
    
    for j in dict1:
        new_dict={}
        if in_count<=out_count:
            in_count+=1
        else:
            new_dict[i]=dict1[i]
            new_dict[j]=dict1[j]
            res.append(new_dict)
    out_count+=1
print(res)
     



