#slicing with strings (both +ve and -ve indexing)
str = "Ali khan, Tappu na vaipu vundhi kabatti....kh"
print(len(str))
print(str[ : ])
print(str[ :-38:3])
print(str[0:42])
print(str[-1:-8:-1])
print(str[-45:-1])
print(str[6:45:6])

#To print memory address of number or string
#Here "id" refers to memory block--> it will print the address of number 5.
num1=5
print(id(num1)) 
str1="pooji"
print(id(str1))
str2="pooji"
print(id(str2))

#Data types
print(type(4))
print(type(4.0))
print(type('c'))
print(type("pooji"))
print(type(5+8j))

#We cannot change substring to existing string, because strings are immutable data type (cannot be change)
str1="Hut"
print(str1[0])
str1[0] = 'C'
print(str1[0]) # It shows TypeError: 'str' object does not support item assignment

#If we need to change character/substring in string, then we need to change entire string and then print using indexing
str1="Cut"
print(str1[0])




