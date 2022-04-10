# Create a dictionary from 2 lists, where the elements of 1st list are the keys and the elements of the 2nd list are the corresponding values.
list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
# dict1={}
# dict1=dict1.fromkey(list1,list2)
# print(dict1)


# dic={}
# for key in list1:
#     for value in list2:
#         dic[key]=value
#         list2.remove(value)
#         break
# print("Resultant dictionary is :" ,dic)  

i=0
dict={}
while i<len(list1):
    dict.update({list1[i]:list2[i]})   
    i+=1
print(dict)   



# Write a Python script to merge two Python dictionaries
