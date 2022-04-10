# Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
dict=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
var={}

for d in dict:
    if d['item'] not in var:
        var[d['item']]=d['amount']
    else:
        var[d['item']]+=d['amount']
print(var)
        