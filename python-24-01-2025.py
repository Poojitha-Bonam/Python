print("----Range----")
print(list(range(0,100,2))) #skips 1 number and then it prints
print(list(range(100,0,-3))) #skips 2 and then prints in reverse order
print(list(range(100,0,-1))) #prints continous and then print in reverse order
print(list(range(100,-1))) #prints empty list (because 1st number is greater than 2nd number, if we need to print then give -1 then it print in reverse order)

list=[1,2,4,6,5,85]
print(len(list))
for i in range(0,len(list)):
    #print(i)
    print(i,list[i])

#for i in range(0,100):
    #print(i)

print("----Dictionary----") #--> Collection of items, which is used to store items in key value pair, we can access through keys only(Mutable data type)
dict={1:'Mahesh Babu',2:'AA',3:'Dhanush',4:'Rajendra Prasad',5:'Snow Family',6:'Surya',7:'Surya'}

print(dict[2])
print(dict)
#Changing the value of key-1
dict[1]='BB2'
print(dict) #It can be change the value of Mahesh babu to BB2 because, dictionary is mutable data type.

#To add key:value pair in dictionary(at the end of dictionary)
dict['key-1']='value-1'
print(dict)

#If we need to update the key-1 value to updated value
dict['key-1']='updated-value-1'
print(dict) # It can be replace in place of value-1

print("----Set----")
#Set-Collection of elements(Unique, Unordered, Finite) and it is Immutable data type

set={2,4,5,2,2,2,2,4,6}
print(set) #Repeated elements will be prints at one time only

print("----None----")
num=5
num=None
print(num)
print(type(num))
print(id(num)) #It prints memeory but there is nothing in this memory, because num stores 'None'

#input()

print(input("Enter a number"))

#refer input to a variable

a=input("Enter a number")
print(a)

a=int(input("Enter a value"))
b=int(input("Enter a value"))
print(a+b)





      


