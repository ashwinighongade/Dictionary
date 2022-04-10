#  Write a Python program to count the frequency in a given dictionary. Go to the editor
# Original Dictionary:
# {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# Count the frequency of the said dictionary:
# # Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})

dict={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
dict1={}

for i in dict:
    count=0
    for j in dict:
        if dict[i]==dict[j]:
            count+=1
        dict1.update({dict[i]:count})
print(dict1)

