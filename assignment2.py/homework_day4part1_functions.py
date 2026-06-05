#functions 
#check whether a no. is positive , negative or zero 
num=int(input("enter a number :"))
def check(num):
    if num>0:
        print(f"{num} is positive")
    elif num==0:
        print(f"{num} is zero")
    else:
        print(f"{num} is negative")
check(num)

#check whether number is even or odd 
num= int(input("enter a number to check even or odd :"))
def check(num):
    if num%2==0:
        print(f"{num} is even ")
    else:
        print(f"{num} is odd ")
check(num)
#fn. which accepts two no. and returns graeater no. 
def greater(a,b):
    if a>b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")
greater(-5,-6)

#check whether a person is eligible to vote (age>=18)
age= int(input("enter your age:"))
def vote(age):
    if age>=18:
        print("you are eligible to vote ")
    else:
        print("you are not eligible to vote ")
vote(age)

#check whether a number is divisible by 5 or not 
num= int(input("enter a number to check divisiblity of 5 :"))
def divisible(num):
    if num%5==0:
        print(f"{num} is divisible by 5 ")
    else:
        print("number is not divisible by 5 ")
divisible(num)

# check whether a given year is leap or not 
year= int(input("enter a year :"))
def leap(year):
    if year%4==0:
        print(f"{year} is a leap year ")
    else:
        print(f"{year} is not a leap year ")
leap(year)

#check whether a character is vowel or consonant 
char=input("enter a character :")
def vowel_or_not(char):
    if char=="aeiouAEIOU":
        print(f"{char} is a vowel ")
    else :
        print(f"{char} is consonant")
vowel_or_not(char)

#find largest among three numbers 
def largest(a,b,c):
    if a>b and a>c :
        print(f"{a} is largest")
    elif b>a and b>c:
        print(f"{b} is largest ")
    else :
        print(f"{c} is largest ")
largest(134, 156, 67)

#calcualte sum of numbers from 1 to 100
def sum_upto_100(n):
    return n*(n+1)//2
print(sum_upto_100(100))

#print multiplication table of number 
def table(num):
    for i in range (1, 11):
        print(f"{num}X{i}={num*i}")
table(17)

#calculate and return square of number 
def square(num):
    return num*num
print(square(11))

#calculate factorial of number 
def fact(n):
    fact=1
    for i in range(n,0,-1):
        fact*=i
        return fact
print(fact(6))

#chck whether a number is prime or not 
def prime(a):
    for i in range(2, a):
        if a%i==0:
            print("no. is not prime")
            break
        else:
            print("no. is prime")
            break
prime(7)

#calculate sum of digits of numbers
def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10   # get the last digit
        sum += digit   # add it to the sum
        n //= 10         # remove the last digit
    return sum

num = int(input("Enter a number: "))
print("Sum of digits of", num, "is:", sum_of_digits(num))

#functions that accepts a number n and returns the sum of all numbers from 1 to n 
def sum_upto_n(n):
    # Using the formula for sum of first n natural numbers
    return n * (n + 1) // 2

# Example usage:
num = int(input("Enter a number: "))
print("Sum from 1 to", num, "is:", sum_upto_n(num))
