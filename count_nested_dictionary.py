a={2:"me","ram":"apple",5:{"sham":"mango",4:{"nam":"raj",5:{"vani":"car"}}}}
count=0
b=str(a)
for i in b:
    if i=="{":
        count+=1
print(count)
