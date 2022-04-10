# Write a program to print the top 3 highest values of a given dictionary.
# my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# list=[]
# for x,y in my_dict.items():
#     list.append(y)
# s=max(list)
# print(s)
# list.remove(s)
# s=max(list)
# print(s)
# list.remove(s)
# s=max(list)
# print(s)

my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
max=0
for i in my_dict.values():
    if i>max:
        max=i
max1=0
for i in my_dict.values():
    if max!=i and max1<i:
        max1=i
max2=0
for i in my_dict.values():
    if max!=i and max1!=i and max2<i:
        max2=i
print(max,max1,max2)
    
    
# print(max,max1)

# # Using Collections.counter() function
# # collections module
# from collections import Counter
# # Dictionary
# my_dict = {'T': 23, 'U': 22, 'T': 21,'O': 20, 'R': 32, 'S': 99}
# k = Counter(my_dict)
# # 3 highest values
# high = k.most_common(3)
# print("Dictionary with 3 highest values:")
# print("Keys : Values")
# for i in high:
#    print(i[0]," : ",i[1]," ")


# # Using nlargest.heapq() function
# # nlargest module
# from heapq import nlargest
# # Dictionary
# my_dict = {'T': 23, 'U': 22, 'T': 21,'O': 20, 'R': 32, 'S': 99}
# ThreeHighest = nlargest(3, my_dict, key = my_dict.get)
# print("Dictionary with 3 highest values:")
# print("Keys : Values")
# for val in ThreeHighest:
#    print(val, " : ", my_dict.get(val))