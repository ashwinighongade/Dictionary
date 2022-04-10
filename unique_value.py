# Take a list having dictionary elements as shown below (Sample Data) and then store all the unique values into a list and print.
# L=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)

# my_dict=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# list1=[]
# for i in my_dict:
#         for j in i :
#             # print(j)
#             if i[j] not in list1:
#                 list1.append(i[j])
# print(list1)
            
my_list=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
d=[]
for i in my_list:
    for j in i:
        if i[j] not in d:
            d.append(i[j])
d= set(d)
print(d)
for dic in my_list:
    # print(dic)
    for y in dic.values():
        if y not in d:
            d.append(y)
d = set(d)
print(d)