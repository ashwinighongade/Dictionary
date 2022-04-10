a={"shopping_list":{"chaco":15,"Bisuits":50,"Diary_milk":30,"ice_cream":20}}
s=input("Enter the key :")
o=int(input("Enter the number :"))
dict1={}
dic={}
add=0
for i in a:
    # print(a[i])
    for j in a[i]:
        if j == s :
            print(j)
            add=a[i][j]+o
            # print(add)
            dic.update({j : add})
        else:
            dic.update({j:a[i][j]})
    dict1.update({i:dic})
print(dict1)
