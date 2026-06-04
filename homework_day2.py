#check whether no.is positive or not 
num=int(input("enter a number for positive or not value : "))
if num>=0:
    print("number is positive")
else:
    print("number is negative")
#chcek whether no. is even or odd 
n= int(input("enter a num for even /odd :"))
if n%2==0:
    print("number is even")
else:
    print("number is odd ")
#find greater no. between two numbers 
a= int(input("enter first no."))
b=int(input("enter second no."))
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is less than {b}")
#chcek whether a person is eligible to vote (age>=18)
age=int(input("enter your age :"))
if age>=18 and 0<age<500:
     print("you are eligible to vote ")
elif age<0 and age<500:
    print("invalid age ")
else:
     print("you are not eligible to vote ")
#chcek whther a no.is divisible by 5 or not 
num=int(input("enter a num to check divisibilty of 5 :"))
if num%5==0:
    print(f"{num} is divisible by 5 ")
else:
    print("not  divisible by 5")
#check whether a given year is leap or not 
year= int(input("enter a year to check leap year or not :"))
if year%4==0 :
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#check  whwther a character is vowel or consonant 
char= input("enter a character to check vowel or consonant :")
if char in "aeiouAEIOU:":
    print(f"{char} is a vowel ")
else:
    print(f"{char} is a consonant")
#assign gradees based on marks 
marks=int(input("enter your marks :"))
if marks>=90:
    print("grade A")
elif (marks>=75 and marks<90):
    print("grade B")
elif (marks >=50 and marks <75):
    print("grade C ")
else:
    print("Fail")
#chcek whwther a number is within range of 1 to 100 
n= int(input("enter a number :"))
if n>=1 and n<=100:
    print(f"{n} is in the range of 1 to 100")
else:
    print(f"{n} is not in the range")
print("""for loop
for loop questions 
""")

#print no. from 1 to 10
for i in range(1, 11):
    print(i)
#print no. from 10 to 1 in reverse manner 
for j in range (10,0,-1):
    print(j)
#print all even no. b/w 1 to 20 
for k in range(1,21):
    if k%2==0:
        print(f"{k} is even")
    else:
        print(f"{k} is odd ")
#print prime no. from 1 to 50
for i in range(1, 51):
    if i>1:
        for j in range (2,i):
            if i%j==0:
                break 
        else:
            print(f"{i} is a prime no.")
#find sum of no. from 1 to 100
sum=0
for i in range(1, 101):
    sum+=i
    print(f"{i} : {sum}")
#find factorial of no. 
n= int(input("enter a number:"))
fact=1
for i in range(1, n+1):
    fact*=i
    print(fact)
# find fibonacci series u to n terms 
n= int(input("enter a number for fibonacci "))
a=0
b=1
for i in range(n):
    print(a)
    a,b=b, a+b
#print multiplication table of no. 
n=int(input("enter a number for table :"))
for i in range(1,11):
    print(f"{n}X{i}={n*i}")
# print each character of string using for loop 
string= input("enter a sentence:")
for ch in string:
    print(ch)
#print pattern using for loop 
n=5
for i in range(n):
    print("*"*(i+1))

#chcek whether no. is prime or not 
a=int(input("enter a no. for prime check :"))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print("no.is not prime")
            break
        else:
            print("no.is prime")
            break
else:
    print("no.is not prime")
print("""while loop 
homework questions 
""")
#print no. from 1 to 10 using while loop 
j=1
while j<=10:
    print(j)
    j+=1
#print no. from 10 to 1 using while loop 
k=10
while k>=1:
    print(k)
    k-=1
#print odd no. from 1 to 20 using while loop 
m=1
while m<=21:
    if m%2==1:
        print(m)
    m+=1
#print sum of no. rom 1 to 50 
sum=0
n=0
while n<51:
    sum+=n
    print(sum)
    n+=1
#count no. of digits in given no. using while loop 
num=int(input("enter a number to count no. of digits :"))
count=0
while num>0:
    num=num//10
    count+=1
    print(count)
#program to reverse a number using while loop 
n= int(input("enter a number for reverse order :"))
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
    print(rev)
#print password of user using while loop only 3 times after that grant denied 
password="admin123"
i=1
while i<=3:
    pwd=input("enter password :")
    if pwd == password:
        print("access granted ")
        print("welcome :)")
        break 
    else:
        print("access denied ")
        print ("try again after some time ")
    i+=1
