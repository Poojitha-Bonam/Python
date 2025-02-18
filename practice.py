# declaration of different datatypes
num=10 #int
num1=58.5 #float
str1="pooji" #string
is_active = True #boolean
list1 = ["apple", "banana", "cherry",['1','2','3']] #list
tup1 = (3, 5) #tuple
dict1 = {"name": "Pooji", "age": 22} #dictionary
s1 = {"red", "green", "blue"} #set
result = None #None

# conditional statements-->if and else statements,elif
# if and else statements
num1=1
if num1==1:
    print("one")
else:
    print("other statements")

# else if (elif) -->
num3 = 1
if num3>1: # if num3 > 0 and num3 != 1:
    print("positive")
elif num3 == 0 :
    print("zero")
elif num3 == 1:
    print("one")
elif num3 == -1:
    print("-1")
elif num3 == -2:
    print("-2")
elif num3 == 1:
    print("one")
else:
    print("negative")

# loops--> while, for
for i in range(0,21):
    print(i)
    print("Hello")
    print("Pooji")
#Even and Odd using for loop
for i in range(0,26):
    if i % 2 == 0:
        print(i, "is an even number")
    else:
        print(i, "is an odd number")

#Even numbers using step
for i in range(0,21,2):
    print(i)

#Odd numbers using step
for i in range(1,21,2):
    print(i)

#Even or Odd using while loop
num = 5
while num < 26:
    if num % 2 == 0:
        print(num,"Even")
    else:
        print(num,"Odd")
    num += 1

# Jump statements-->break, continue
# break
for i in range(0,21):
    print(i)
    if i == 2:
        break
# continue
for i in range(0,10):
    if i == 5: # when we use continue then it will not execute, next statements, so it skips 5
        continue
    print(i)

# functions--> Declaring a functiom and call a function, return statement usage
def sumOfTwoNumbers(a,b):
    print("sum of two numbers is",a+b)
sumOfTwoNumbers(2,3)

def even_or_odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(25))

# inbult functions-->Atleast most famous one-->string and list
text="Python"
# print(text[-1])
print(text[2:6])

s1=" pooji "
s2="Bonam"
print(s1+" "+s2)
print(s1 * 3)
print(s1.strip())
print(s1.lower())
print(s1.upper())
print(s1.find("oo"))
print(s1.replace(" pooji ","Pooji"))
print(s2.split(","))
s3=["Bonam","23"]
print(",".join(s3))
list=[1,2,3]
list.append(2)
print(list)

numbers=[1,2]
print(numbers[1])
print(numbers[0:2])
print(len(numbers))
print(2 in numbers)
l1=[1,2,3,4]
l2=[4,3,2,4]
print(l1+l2)
l1.extend([2,3])
print(l1)
l1.insert(4,8)
print(l1)
l1.pop(3)
print(l1)
print(l1.index(3))
l1.reverse()
print(l1)
l1.sort()
print(l1)

s1={1,2}
s5={2,3}
s6={3,4}
s7={7,8,4}
print(s1.union(s5,s6,s7))
l={1,2,3,4}
l.clear()
print(l)

set1={1,2,3,4,5,2}
set2={2,3,6,8,3,4,9}
print(set1 | set2)

set1={1,2,3,4}
set2={1,2,3,4,5,6,74,56}
print(set2.union(set1))




