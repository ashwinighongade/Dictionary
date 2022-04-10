# Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
dict= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
a=''
for x,y in dict.items():
    if y>max:
        max=y
        a=x
max1=0
b=''
for y in dict.values():
    if y>max1 and max!=y:
        max1=y
        b=x
max2=0
c=''
for y in dict.values():
    if y>max2 and max!=y and max1!=y:
        max2=y
        c=x
print(a,max)
print(b,max1)
print(c,max2)

