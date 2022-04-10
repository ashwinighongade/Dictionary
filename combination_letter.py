# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
dict= {'1':['a','b'], '2':['c','d']}
for x in dict['1']:
    for y in dict['2']:
        print(x+y)


# for x,y in dict.values():
#     print(x,y)
        
# dict= {'1':['a','b'], '2':['c','d']}
# from itertools import product
# for x, y in product(*dict.values()):
#     print(x + y)
