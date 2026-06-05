#function 
def Hello():
    print("hello")
Hello()

def Value():
    a=10
    b=20
    return a+b
print(Value())
#function with parameters &arguments
def add(a,b): #parameters
    return a+b
print(add(6,7)) #arguments 


#data structure in python 
li=[1, 2, 4.67, 3.142,"priya", "kanan"]
print(li[3])
for i in li:
    print(i)
li.append("khushi")
li.append("kashish")
print(li)
li.extend(["siya"])
print(li)
li.insert(1,"november")
print(li)
tup=(1,3,4)
tup1=(5,"sarita",8.9)
print(tup+tup1)
print(tup[0])
print(tup1[2])
tup2=tup+tup1
print(tup2[1:])
print(tup2*5)
print("kanan" in tup)
