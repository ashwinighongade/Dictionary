# output={"A":[7,0,9,3],"B":[5,4,2,6]}
dic={"A":[3,9,0,7],"B":[6,2,4,5]}
dict={}
for x,y in dic.items():
    s=[]
    a=''
    if type(y)==list:
        a=x
        # print(a)
        i=1
        while i<len(y)+1:
            s.append(y[-i])
            i+=1
            dict.update({a:s})
print(dict)
            
