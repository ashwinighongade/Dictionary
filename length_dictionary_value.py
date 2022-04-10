# Q48.Write a Python program to find the length of a given dictionary values. 
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary
dict={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Length of dictionary values:
# {'Austin Little': 13, 'Natasha Howard': 14, 'Alfred Mullins': 14, 'Jamie Rowe': 10}
# dict={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dict1={}
for x in dict:
    d=len(dict[x])
    print(d)
    dict1.update({dict[x]:d})
print(dict1)
