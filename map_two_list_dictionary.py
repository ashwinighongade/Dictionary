# Write a Python program to map two lists into a dictionary.
x = ['key1', 'key2', 'key3']
y = [1,2,3,]
dict={}
i=0
while i<len(x):
    dict.update({x[i]:y[i]})
    i+=1
print(dict)