# output={0:2,1:6,2:11,3:18}

a=[2,4,5,7]
# my_dict={}
# sum=0
# i=0
# while i<len(a):
#     sum+=a[i]
#     # print(sum)
#     my_dict.update({i:sum})
#     i+=1
# print(my_dict)
dict={}
sum=0
for i in range(len(a)):
    sum+=a[i]
    dict[i]=sum
print(dict)