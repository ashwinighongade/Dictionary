# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# dict1={0:10,1:20}
# dict1[2]=30
# # dict1.update({2:30})
# print(dict1)
dict1={0: 10, 1: 20}
for i in range(2):
    key=int(input("Enter the key"))
    value=int(input("Enter the value"))
    dict1.update({key:value})
print(dict1)
# dict1={0: 10, 1: 20}
# while True:
#     input1=(input("please enter the key and value separated by comma or q to exit :"))
#     if input1=="q":
#         break
#     key,value=input1.split(",")
#     dict1.update({key:value})
# print(dict1)