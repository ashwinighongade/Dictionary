student_details={}
for i in range(10):
    input_u=input("Enter the name and marks separated by comma :")
    name,marks=input_u.split(',')
    student_details.update({name:marks})
print(student_details)

# d={"john":40,"peter":45}
# if "john" in d:
#     print(d["john"])