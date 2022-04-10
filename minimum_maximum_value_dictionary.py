# Write a Python program to get the maximum and minimum value in a dictionary.
dict1={'w':23,'x':43,'y':34,'z':51,'v':74,'n':15}
list1=[]
for i in dict1.values():
    list1.append(i)
print(list1)
max=0
min=list1[0]
for i in list1:
    if i>max:
        max=i
    if i<min:
        min=i
print(max) 
print(min)   