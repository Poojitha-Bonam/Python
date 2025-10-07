
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7]
y=[10,22,35,40,32,17,78]

plt.plot(x,y)
plt.title('Students Marks')
plt.xlabel('Roll No')
plt.ylabel('Marks')
# plt.plot(x,y,color='#FF5733',linestyle='--',marker='s')

# color = red,purple,yellow, #FF5733

# marker=
# 'o' -->circle
# 's' -->square
# '^' --> triangle up
# 'v' --> Triangle down
# '*' --> star
# '+' --> plus
# 'x' --> cross
# 'd' --> diamond
# 'p' --> pentagon

# linestyles =
# '-' --> solid (by default)
# '--' --> dashed
# '-.' --> dashdot
# ':' --> dotted

# shortcut --> works only for straight colors like red, purple etc..
plt.plot(x,y,'ro--',label='y graph') #color marker linestyle
# label is used to identify a particular plot

# multiple plots on same graph
y2=[i*2 for i in y]
plt.plot(x,y2,'bs--',label='y2 graph')

plt.legend() #--> to show labels in graph (by default location is upper left)
# we can change location of labels using below
# plt.legend(loc='lower right')


# sine plot
a=np.linspace(0,10,100)
b=np.sin(a)
c=np.cos(a)
plt.plot(a,b,label='sine')

# cos plot
plt.plot(a,c,color='red',label='cos')
plt.legend() # for label

# Bar graph

names=['Pooji','Chinnu','Nani']
marks = [60,75,95]
plt.bar(names,marks, color='purple')

# Scatter plot -->it consists only points, doesnot joint points

d=np.linspace(0,10,100)
e=np.sin(d)
plt.scatter(d,e)

# pie chart

industry = ["Agriculture", "Industrial", "Service sector"]
values = [25,25,50]
plt.pie(x=values,labels=industry,autopct='%1.2f%%')
plt.savefig('Sectordp.png') #--> it is used to save above pie chart as image

# sub plots: It is used to represent more plots separately in single graph
# It returns 2 values (fig and arr)
m=[1,2,3,4]
n=[2,3,5,7]

industry = ["Agriculture", "Industrial", "Service sector"]
values = [25,25,50]

fig,arr=plt.subplots(1,2) # 1 row and 2 cols
arr[0].plot(m,n) #in 0th col
arr[1].pie(x=values,labels=industry) #in 1st col

#  for multiple rows and cols
fig,arr=plt.subplots(2,2)
arr[0][0].plot(m,n)
arr[0][0].set_title('Marks') #--> gives title to each graph
arr[0][0].set_xlabel('Roll No')
arr[0][0].set_ylabel('Roll No')

arr[0][1].pie(x=values,labels=industry) 
arr[0][1].set_title('Industry')

arr[1][0].pie(x=values,labels=industry) 
arr[1][0].set_title('Industry')

arr[1][1].plot(m,n)
arr[1][1].set_title('Marks')

# plt.figure(figsize=(9,9)) --> To adjust the size of a plot

plt.show()
