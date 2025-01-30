#Logical operators --> and, or, not
#and: If both values are 1 then it gives 1

print(True and True)
print(False and True)
print(True and False)
print(False and False)
print(False and (True and True))


print(2 and 3) #3 --> If first value is truthy value, then output depends on 2nd value i.e., 3 so, it will print output as 3
print(3 and 2)  #2 --> If first value is truthy value, then output depends on 2nd value i.e., 2 so, it will print output as 2
print(3 and "")
print("" and 0) #(empty string) --> If any value is falsy value, then output depends on 1st value i.e., "" so, it will print output as ""
print(0 and "")
print(-3 and -2) #-2
print(False and 58)
print(-58 and 85) #85

#or: If any one value is 1 then it gives output as 1

print(True or False)
print(False or True)
print(True or (False and True))
print(True and (False or True) and (False or True))


print(2 or 3)
print(3 or 2)
print("" or True)
print(0 or 0 or 1)
print(-1 or -9)

#Not: If we give False then it will give output as True and viceversa.,

print(not True)
print(not False)
print(not (2 or 3))
print(not not("" and 3))


#Bitwise Operators --> &,|,^,<<,>>,~
#&
      
print(4 & 3) #0
#0100 & 0011 ==> 0000 = 0
print(14 & 12)
#1100 & 1110 ==> 1100 = 12

#|
    
print(12 | 14)
#1100 | 1110 ==> 1110 = 14

#Xor Operator

print(12 ^ 14)
#1100 ^ 1110 ==> 0010 = 2

#Left Shift --> 

print(3 << 1) # multiplied double, if if we mention right side value as 1
print(2 >> 1) # gives half of number and gives quotient as output i.e., 2 and gives only integer values

print(4 << 1)
print(4 >> 1)

print(29 << 1)
print(29 >> 1)

#Right Shift --> discards last nunber and then shifts one bit to the right side

#001011
#000101

#~ --> it gives +1 to the given number and then gives -ve number














