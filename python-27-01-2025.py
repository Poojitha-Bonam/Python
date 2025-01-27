#Naming Convension --> It is used to represent the code quality.
#Pascal Case, Snake Case, Camel Case

# 1.Pascal Case --> 1st letter of each word should be starts with "Capital letter", It can be used in classes.
#Eg: humanbeing - HumanBeing, addfunction - AddFunction

# 2.Snake Case --> '_' should be written between two words, and all letters should be in small letters. We can use Snake Case in Variables and Function name.
#Eg: humanbeing - human_being, addfunction - add_function

# Camel Case --> 1st letter of 2nd word should be starts with "capital letter".
#Eg: humanbeing - humanBeing

#Rules
#------

# 1. Try to follow pascal case or snake case
# 2. Try to give some context while defining variables
# 3. Constants --> All capitals letters should be write to represent the constants
    #Eg: DB_PASSWORD = '123456'

# Conversion of data types:
    # Eg: String to int, range to list, bool to int
# 1. Numeric
print("-----int to float-----")
int1 = 5
print(float(int1))

print(int(int1)) # again conversion of float to same integer

int2 = 5.9
int2 = int(int2)
print(int2)

int2 = float(int2)
print(int2)

print("-----bool to int-----")

bool1 = True
print(int(bool1))

print("-----int to bool-----")
print(bool(1))
print(bool(0))
print(bool(2))
print(bool(-1))
print(bool(-22))

# Thruthy values and Falsy values
    # Thruthy values - (All numbers execept 0)accepts True, Strings  
    # Falsy values - 0, False, ''

print("-----Bool to String-----")
print(bool("    "))
print(bool('Hello'))
print(bool(''))

print("-----String to int-----")
print(int('25'))
#print(int('25a'))
print(int(float('25.555')))

print("-----String to float-----")
int2 = '5.555'
print(float(int2))
print(float('25.555')

print("-----String to List-----")
str1 = "Chinnari Pelli Kuthuru"
print(list(str1))
print(len(list(str1)))

list1 = [1,2,True,[1,6.72]]
str1 = str(list1)
print(str1)
print(str1[0]) # It prints '['







