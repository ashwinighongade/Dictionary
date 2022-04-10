# Write a program to print the top 3 highest values of a given dictionary.
my_dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
max=0
a1=""
max1=0
b1=""
max2=0
c1=""
for x,y in my_dict.items():
    if max<y:
        max=y
        a1=x
for x,y in my_dict.items():   
    if max!=y and max1<y:
        max1=y
        b1=x
for x,y in my_dict.items(): 
    if max!=y and max1!=y and max2<y:
        max2=y
        c1=x
print(a1,":",max,b1,":",max1,c1,":",max2)
    