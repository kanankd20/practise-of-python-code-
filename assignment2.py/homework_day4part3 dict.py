#store student name , age and city 
dict={"name":"kanan","age":19,"city":"jalandhar"}
print(dict)

# print all keys of dictionary 
print(dict.keys())

#print all values 
print(dict.values())

#add new key value pair to an existing dictionary 
dict["id"]=2322661
print(f"updated dictionary:{dict}")

#update value of a existing key 
dict["age"]=20
print(f"updated value of age:{dict}")

#check whether key exists or not 
print("profession"in dict ) 

#remove a key - value pair from dictionary 
del dict["id"]
print(dict)

#count total no. of key value pairs 
print(len(dict))

#iterate through dict and print all keys and their values 
for i in dict.items():
    print(i)
    
#creating a dict of student names and marks , and then find student with highest marks 
marks={"kanan":90,"kashish":80,"priya":95,"khushi":76}
for i in marks.items():
    print(i)
print(f"max marks of {max(marks.keys())}:{max(marks.values())}")
    