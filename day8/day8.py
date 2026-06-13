# file= open("file.txt","w")
# file.write("hello world ")
# file.write("welcome to python")
# file.close()
# print(file)

# file=open("file.txt","r")
# print(file.read())
# file.close()

# file=open("file.txt","a")
# file.write(f"\nWelcome to advanced python session")
# file.close()
# print(file)

# file=open("file.txt","r")
# print(file.read())
# file.close()

#delete file contents 
# import os
# os.remove("file.txt")

# #exception handling 
# try:
#     num=int(input("enter a number :"))
#     result=10/num 
# except ZeroDivisionError:
#     print("cant divide by zero ")
# except ValueError:
#     print("enter only number values")
# else:
#     print("no error occured:)")
#     print(f"result is :{result}")
# finally:
#     print("thank you for using program ")
# #it will show an error if some incertain value is added like zero to handle , we use exception handling 
# # print(result)

#read file line by line using loop 
# file=open("file.txt","w")
# file.write("\n welcome to python ")
# file.write("\n I am writing content in file to understand file system in python .")
# file.write("\n These content really helps us a lot :)")
# file.close()

# file = open("file.txt", "r")
# for line in file:   # iterate directly over file object
#     print(line.strip()) 
# file.close()

# #oops concept 
# class Student:
#     def __init__(self, name, age, id, grade):
#         self.name=name
#         self.age=age
#         self.id=id
#         self.grade=grade
#     def show_student(self):
#         print(f"name :{self.name}")
#         print(f"age:{self.age}")
#         print(f"id :{self.id}")
#         print(f"grade :{self.grade}")
# s1=Student("kanan", 19,2322661, "A")
# s1.show_student()

# class Employee:
#     def __init__(self, name,id, salary):
#         self.name=name
#         self.id=id
#         self.salary=salary
#     def show_emp(self):
#         print(f"name:{self.name}")
#         print(f"id:{self.id}")
#         print(f"salary:{self.salary}")
# e1=input("enter name of an employee:")
# e2=int(input("enter employee id :"))
# e3=float(input("enetr salary :"))
# e4=Employee(e1,e2,e3)
# e4.show_emp()

#inheritance concept
# class Animal:
#     def sound(self):
#         print("makes sound")
# class Tiger(Animal):
#     def roar(self):
#         print(" Tiger roars")
# a1=Tiger()
# # a1.sound()
# a1.roar()
# a1.sound()

# #polymorphism 
# class Animal:
#     def sound(self):
#         print("makes sound")
# class Dog(Animal):
#     def sound(self):
#         print("dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("cat meows")
# for Animal in [Dog(),Cat()]:
#     Animal.sound()

# #encapsulation
# class BankAccount:
#     def __init__(self, name,balance):
#         self.name=name
#         self.balance=balance
#     def get_balanced(self): #getter method to access private attribute 
#         return self.balance
    
# account=BankAccount("kanan",10000)
# print(account.get_balanced())

#abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length 
        self.width = width
    def area(self):
            return self.length*self.width
rect=Rectangle(10,20)
print(rect.area())


        
