print("-----Number system-----")
# Base --> we can generate every other number using that base

#Decimal
#Eg: 199 - 1*100 + 9*10 + 9*1
#Eg: 1239 - 9*1 + 3*10 + 2*100 + 1*1000

#Possible numbers in decimal number system is 0 to 9

# Binary --> Binary possible values are 0 and 1
        #Binary to Decimal
    #Eg: 101101 - 1*2^0 + 0*2^1 + 1*2^2 + 1*2^3 + 0*2^4 + 1*2^5 (Ans:45)
    #Eg: 1111101 - 1*1 + 0 + 1*4 + 1*8 + 1*16 + 1*32 +1*64 (Ans:125)

#Octagonal --> Octogonal possible values are 0 to 7
        #Octogonal to Decimal
    #Eg: 1256 - 6*8^0 + 5*8^1 + 2*8^2 + 1*8^3 (Ans:686)

#Hexadecimal --> Hexadecimal possible values are 0 to 15
#10-A
#11-B
#12-C
#13-D
#14-E
#15-F
        #Hexadecimal to Decimal
    #Eg: AF1 - 1*16^0 + 15*16^1 + 10*16^2 (Ans:2801)

#Eg: 111
# binary - 1*2^0 + 1*2^1 + 1*2^2 -->7
#Octogonal - 1*8^0 + 1*8^1 + 1*8^2 -->73
#Hexadecimal - 1*16^0 + 1*16^1 + 1*16^2 -->272

 #To convert decimal to bin, oct, hex
num=84
print(bin(num))
print(oct(num))
print(hex(num))

 # To convert binary to decimal
print(int(0b1010100))

 # To convert octal to decimal
#print(0o124)
print(int(0o124))

 # To convert Hexadecimal to decimal
print(int(0x54))

print("-----Operators-----")
#Arithmetic Operators --> +, -, *, /, %, //, **
#Relational Operators --> <, >, <=, >=, ==, !=

print(2>3)
print(2<3)
print(2<=3)
print(2>=3)
print(2!=3)
print(2==3)

#Assignment Opeartors --> =, +=, -=, *=, /=, //
n=3
n+=1
print(n)

n1=6
n1-=1
print(n1)

n2=6
n2*=4
print(n2)

n3=6
n3/=2
print(n3)

n4=6
n4//=2
print(n4)

a=5
a-=-1
print(a)







