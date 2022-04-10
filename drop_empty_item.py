# Q38.. Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}
dict={'c1': 'Red', 'c2': 'Green', 'c3': None}
b={}
for x,y in dict.items():
    if y==None:
        pass
    else:
        b.update({x:y})
print(b)