# Write a Python program to remove duplicates from Dictionary.
student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 
    'subject_integration': ['english, math, science']},
 'id2': {'name': ['David'], 'class': ['V'], 
    'subject_integration': ['english, math, science']},
 'id3': {'name': ['Sara'], 'class': ['V'], 
    'subject_integration': ['english, math, science']},
 'id4': {'name': ['Surya'], 'class': ['V'], 
    'subject_integration': ['english, math, science']},}
dict={}
n=student_data['id1']
for i in student_data:
   # print(i['id2'])
   if student_data[i]!=n:
      dict.update({i:student_data[i]})
   n=i
print(dict)
