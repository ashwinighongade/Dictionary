# Write a Python program to multiply all the items in a dictionary.
dict={"value1":5, "value2":4, "value3":3, "value4":2, "value5":1}
fac=1
for x in dict:
    fac=fac*dict[x]
print(fac)