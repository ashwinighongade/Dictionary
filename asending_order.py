# Write a program to sort a dictionary in ascending or descending according to its values
a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':30}
for i in a:
    for j in a:
        if a[j]>a[i]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
print(a)
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# s= sorted(d.items())
# print('ascending order : ',s)
# # s1= dict( sorted(d.items(),reverse=True))
# print('descending order : ',s1)

