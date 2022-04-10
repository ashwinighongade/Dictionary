# 52. Write a Python program to extract a list of values from a given list of dictionaries. Go to the editor
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Science
# [92, 94, 88]
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Math
# [90, 89, 92]

# dict1=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# list1=[]
# list2=[]
# for i in dict1:
#     for j in i:
#         a=(i['Science'])
#         b=(i['Math'])
#     list1.append(a)
#     list2.append(b)
# print(list1)
# print(list2)


# Write a Python program to extract values from a given dictionaries and create a list of lists from those values. Go to the editor
# Original Dictionary:
# [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# Extract values from the said dictionarie and create a list of lists using those values:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# [[1, 'Jean Castro'], [2, 'Lula Powell'], [3, 'Brian Howell'], [4, 'Lynne Foster'], [5, 'Zachary Simon']]
# [['Jean Castro', 'V'], ['Lula Powell', 'V'], ['Brian Howell', 'VI'], ['Lynne Foster', 'VI'], ['Zachary Simon', 'VII']]

dict1={'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
list1=[]
list2=[]
list3=[]
for i in dict1:

    a=[i['student_id'],i['name'],i['class']]
    b=[i['student_id'],i['name']]
    c=[i['name'],i['class']]
    list1.append(a)
    list2.append(b)
    list3.append(c)
print(list1)
print(list2)
print(list3)