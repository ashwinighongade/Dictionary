# Write a Python program to sort a list alphabetically in a dictionary.
# word=['bat','cat','mat','rat']
# for i in range(0,len(word)):
#     for j in range(0,len(word)):
#         if word[j]>word[i]:
#             tem=word[i]
#             word[i]=word[j]
#             word[j]=tem
# print(word)


dict={1:'deepa',2:'ram',3:'shyam',4:'kavita',11:'Banu',5:'anu',6:'priti',7:'yogi',8:'banu'}
dict1={}
list1=[]
for x in dict:
    list1.append(dict[x])
    # print(list1)
for i in range(0,len(list1)):
    for j in range(0,len(list1)):
        if list1[j]>list1[i]:
            tem=list1[i]
            list1[i]=list1[j]
            list1[j]=tem
print(list1)
for i in list1:
    for x in dict:
        if dict[x]==i:
            dict1[x]=i
            # dict1.update({x:i})
print(dict1)
    
    


