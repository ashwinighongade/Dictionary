dict1={"a":20,20:{"A":30,"c":30,10:20},5:{"v":2,4:"s"}}

sum=0
for i in dict1:
    if type(dict1[i])==int:
        sum+=dict1[i]
    if type(i)==int:
        sum+=i
    if type(dict1[i])==dict:
        for j in dict1[i]:
            if type(j)==int:
                sum+=j
            if type(dict1[i][j])==int:
                sum+=dict1[i][j]
print(sum)       
