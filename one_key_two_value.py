list=[]
a={"name":"rupa","friends":"sneha"}
list.append(a["friends"])
a["friends"]="ashwini"
list.append(a["friends"])
a.update({"friends":list})
print(a)
