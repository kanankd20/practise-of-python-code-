for i in range(1,10): #simple for loop
    print(i)
for j in range(1, 11, 2): #for loop with one skip iteration 
    print(j)
for k in range(10,-1,-1): #for loop with reverse iteration 
    print(k) 
    #print table 

for i in range(3,21,3):
    print(i)
# print dynamic table of 5 
n=int(input("enter number for table :"))
for i in range(n,(n*10+1),n):
    print(i)
#print formatted table 
n=int(input("enter a number for formatted table :"))
for i in range(1,11):
    print(f"{i}X{n}={i*n}")
# using for loop to print patterns 
n=6
for i in range(1,n+1):
    print("k"*i)
for j in range(1,10):
    if j==7:
        break
    print(j)
for m in range(1,20):
    if m%2==0:
        continue
    print(m)
music= "prem ki leela"
for i in range(len(music)):
    if music==" ":
        continue
    print(music[i])
    
#while loop 
a=4
while a<10:
    print(a)
    a+=1
x=1
while x<=21:
    if x%2 == 0:
        print(x)
    x+=1
password = "admin12345"
user_input=""
while user_input !=password :
    user_input=input("enter your password:")
print("welcome to ur account")
    