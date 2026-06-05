#create a list of number and print all elements 
li=[1,2,3,4,5,6,7,8,9,10]
for i in li:
    print(i)

#print largest element in list 
li1=[12, 14, 7.8, 56]
print(max(li1))

#find smallest element in list 
print(min(li1))
#print sum of all elements of list 
print(sum(li))
print(sum(li1))
 #find average of all elements of list 
print(sum(li)/len(li))
#count how many even numbers are present in list 
count=0
for i in li1:
    if i%2==0:
        count+=1
    print(count)

#create a new list containing only odd numbers from an existing list
count=0
li2=[]
for i in li1:
    if i%2==1:
        count+=1
        li2.append()
print(li2)

#program to find element is present in list or not
print(4 in li)
 
#program to reverse a list without using built in reverse functions 
li3=[1,2,3,4,5]
li4=[]
for i in range(len(li3)-1,-1,-1):
    li4.append(li3[i])
print(li4)

#find second largest element in list 
li.sort()
print(li[-2])
