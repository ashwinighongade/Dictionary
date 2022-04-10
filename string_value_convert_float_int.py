# Q46.Write a Python program to convert string values of a given dictionary, into integer/float datatypes. Go to the editor
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# list1=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
# list1=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
list1=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
ans_list=[] 
dict1={}
dict2={} 
# a,b=list1 
a=list1[0]
b=list1[1]
for i in a:
    c=float(a[i])
    d={i:int(c)}
    dict1.update(d)
for j in b:
    d=float(b[j])
    d1={j:int(d)}
    dict2.update(d1)
# print(dict2)
ans_list.append(dict1)
ans_list.append(dict2)
print(ans_list)
