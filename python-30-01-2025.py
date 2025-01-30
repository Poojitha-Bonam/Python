print("-----Control Statements-----") #--> controls the flow of execution of a code.

#There are 3 types of control statements --> conditional statements, Loops and Jump statements

# Conditional statements

# num1=1
# if num1==1:
#     print("Pushpa The Rise")
# else:
#     print("Pushpa The Rule")


# num2=8
# if num2>0: 
#     print(num2, "is a positive") 
# else:
#     if num2==0:
#         print(num2, "is neither positive nor negative") 
#     else:
#         if num2==1:
#             print(num2,"one")
#         else:
#             if num2==-1:
#                 print("-1")
#             else:
#                 print(num2, "is a negative")

# # else if (elif) -->
# num3 = 1
# if num3>1: # if num3 > 0 and num3 != 1:
#     print("positive")
# elif num3 == 0 :
#     print("zero")
# elif num3 == 1:
#     print("one")
# elif num3 == -1:
#     print("-1")
# elif num3 == -2:
#     print("-2")
# elif num3 == 1:
#     print("one")
# else:
#     print("negative")



# Current Bill
#100 units <= 100-->per unit 50rs
#101 to 200 --> per unit is 100rs
#201 to any number --> per unit is 150rs

current_units=int(input("Enter Units"))
if current_units<=50:
    print("0")
else:
    if current_units<=100:
        if current_units < 0:
            print("Invalid")
        else:
            a=current_units*50
            print(a)
    else:
        if current_units>=101 and current_units<=200:
            a=current_units*100
            print(a)
        else:
            print(current_units*150)

#Loops -->