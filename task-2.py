# 1.To print 1 to 100 numbers using while loop
n=0
while n<100:
    n=n+1
    print(n)

# 2.To print 1 to 100 numbers in reverse order using for loop and while loop
# Using while loop
n=101
while n>0:
    n=n-1
    print(n)

# Using for loop
for i in range(100,0,-1):
    print(i)

# 3.To reverse a number using while loop without string conversion input:1234, output:4321
num=1234
rev_num=0
while num!=0:
    digit=num%10
    rev_num=rev_num*10+digit
    num//=10
print(rev_num)
