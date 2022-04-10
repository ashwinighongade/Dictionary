# Write a Python program to check all values are same in a dictionary. Go to the editor
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
dict={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
n=12
for x in dict:
    if dict[x]==n:
        print("True")
    else:
        print("False")
        
   