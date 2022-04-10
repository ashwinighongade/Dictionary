# Store the unique letters and their frequency of the letters from the word "MISSISSIPPI" to a dictionary, were the letters are the keys and their frequencies are the values.
a="MISSISSIPPI"
b={}
for i in a:
    if i not in b:
        b[i]=0
    b[i]+=1
print(b)