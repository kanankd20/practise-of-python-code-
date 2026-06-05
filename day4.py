#dictionary
person={"name":"kanan","age":19, "country":"india"}
print(person)
person["profession"]="student"
print(person["profession"])
print(f"updated dictionary :{person}")
print(person.keys())
print(person.values())
for i in person:
    print(i)
for j in person.values():
    print(j)
for i in person.items():
    print(i)
    
    
#dictionary operations 
person.pop("country") #delete 1st option
del person["age"] #delete 2nd option
print(person)
person.clear()#clear all 
