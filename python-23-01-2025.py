#complex numbers
a=5+8j
b=8+5j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
#print(a%b) #unsupported operand type(s) for %: 'complex' and 'complex'
#print(a//b) #It shows TypeError: unsupported operand type(s) for //: 'complex' and 'complex'

#Booleans - True or False
a=294
print(a==293)
print(a==294)
print(94>93)
print(93>94)
print(93>=93)
print(int(False))
print(int(True))

#Sequences - Strings, List, Tuples, Range

#List- List is a ordered collection of data items and can be changeable (Mutable)
list=[0,3,4,'String',True,[1,"Hello",3]]
print(id(list)) #for memory address
print(type(list))
print(len(list))
print(list)
print(list[3]) #indexing in list
print(list[5])

#print(list[6]) #shows IndexError: list index out of range, because the given list consists of only 5 indices

print(list[0:8:2])
print(list[-5])
print(list[5][1]) #Accessing list inside list
print(len(list[5])) #length of list inside list
list[4]="False" #changing the value of index 4,list is a mutable datatype so, it can be change.
print(list)
list[5][1]="Bye" #changing the value of index 1 inside index 5
print(list[5])
print(len(list[5][1])) #length of "hello" insode inner list

#Tuple - Tuple is ordered collection of data items but unchangeable (Immutable)
tuple=(1,2,3,4.5,[1,2,3],"String")
print(tuple)
print(id(tuple)) #for memory address
print(type(tuple))
print(len(tuple))
print(tuple[4])
print(tuple[-4])

#tuple[3]='5'
#print(tuple) #It shows TypeError: 'tuple' object does not support item assignment, because tuple is immutable(cannot be change)

#Range - Limit
print(list(range(0,100))) #To change range into list
print(list(range(1,100,2))) #2 refers ot step, it skips "1 index"
print(list(range(100,1,-1))) #Negative indexing








