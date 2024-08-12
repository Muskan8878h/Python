a={"name":"harsh","age":15,"country":"India "}
a["name"]="nikhil"
print("dict",a)

b=a.keys()
print("all keys",b)

c=a.values()
print("all values",c)

a.copy()
print("copy of a",a)

a.pop("country")
print("remove",a)

#a.clear()
#print("clear all",a)

x=a.items()
print("all keys",b)

a1={"girl":"boy","father":"mother","bro":"sis"}
a.update(a1)
print(a)

keys={1,2,3,4}
values={"hello","hi","how","you"}
a={k:v for(k,v) in zip(keys,values)}
print(a)

a=dict(zip(keys,values))
print(a)

dict1={"Name":"Neha","Roll no":835}
dict1.pop("Roll no")
print(dict1)
dict1.clear()
print(dict1)

dict1={"Name":"Neha","Roll no":835}
dict1["Roll no"]=30
print(dict1)