# 60. Write a Python program to find shortest list of values with the keys in a given dictionary. Go to the editor
# Original Dictionary: {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} Shortest list of values with the keys of the said dictionary: ['VI', 'VIII', 'X']

dict1={'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
for i in dict1:
    a=""
    min=len(dict1[i])
    if len(dict1[i])<min:
        min=len(dict1[i])
list1=[]
for k in dict1:
    if len(dict1[k])==min:
        list1.append(k)
print(list1)

    