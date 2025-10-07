# pandas
# pip install pandas
# Pandas is an open-source Python library built on top of NumPy, designed for data manipulation, analysis, and cleaning.
# It provides two main data structures:
# Series → 1D labeled array
# DataFrame → 2D labeled tabular data (like an Excel sheet)
# Pandas is majorly used for handling 2D data structures called DataFrames.

import pandas as pd
s1=pd.Series([10,20,30], index=['a','b','c'])
print(s1['a'])

# Data Frame : # we can create Data frame using by creating dictionary or file.

# using dictionary
data={
    'name':['pooji','nani','chinnu'], # all arrays must be in same length
    'age':[23,26,27],                 # all arrays must be in same length
    'gender':['F','M','M']            # all arrays must be in same length
} 
df=pd.DataFrame(data)
print(df) # It will create a table form (keys will form as column names)

# output:
#      name  age gender
# 0   pooji   23      F
# 1    nani   26      M
# 2  chinnu   27      M

print(df['name'])
# output:
# 0     pooji
# 1      nani
# 2    chinnu
# Name: name, dtype: object

print(df['age'].mean())
# output: 25.333333333333332


# using files
# read_csv, read_excel, read_json

# Read data from csv
df=pd.read_csv('libraries_file\data.csv')
print(df)


# convert DataFrame to csv
# Creates a file with filename student_details and converts DataFrame to csv in that file

# df=pd.DataFrame(data)
# print(df)
# df.to_csv('Student_details',index=False) #index=False means it ignores indexes column in table


# Data Exploration
print("--------head----------")
print(df.head(2)) # Gives only 2 members data from 1st

print("--------tail----------")
print(df.tail(2)) # Gives only 2 members data from last

print("--------shape----------")
print(df.shape) #5 rows and 4 cols


print("--------info----------")
print(df.info()) #It gives high level information about dataFrame


print("--------describe----------")
print(df.describe()) #It gives high level complete information about dataFrame like count, min, max etc


print("--------dtypes----------")
print(df.dtypes) #gives datatypes of columns

print("--------columns----------")
print(df.columns) #returns cols in list format

print("--------index----------") #RangeIndex(start=0, stop=5, step=1)
print(df.index) #used to iterate for loop

print("--------indexing and selection----------")
print(df['Age'])

print(df[['Age','Name']])

print("--------loc[index,column]----------")
print(df.loc[0,'Name']) #It gives 1st name in names column in csv file

print(df.loc[[0,1,2],'Name']) 

print(df.loc[[0,1,2],'Age'])

print(df.loc[[0,1,2],['Name','Age']]) 

print("--------iloc[index,col_index]----------")
print(df.iloc[0,0]) #In cols place we need to give column_index

# Gives data who are having age more than 25
print(df[df['Age']>25])

print("--------Query----------")
print(df.query('Age>30'))

print("--------Aggregations and grouping----------")
print(df["Age"].mean())
print(df["Age"].sum())
print(df["Age"].value_counts()) #gives count of each age


print(df.fillna(0)) # it is used to fill '0' inplace of 'NaN', 
print(df) #but it will not replace in original dataframe

# If we need to change original dataframe follow below
print(df.fillna(0,inplace=True))


print(df.dropna()) # It is used to drop the data where NA exists,
print(df) #but it will delete original dataframe

# if we need to delete in original dataframe use below
print(df.dropna(inplace=True))

print(df.duplicated()) #To find duplicates 
print(df.drop_duplicates()) #To remove duplicates 
print(df) #(This will also not affect original datatframe) 

# if we need to delete duplicates in original dataframe use below
print(df.drop_duplicates(inplace=True))

# axis = 0 operate down the rows (affects columns i.e gives results in columns)
# axis = 1 operate across the columns (affects rows i.e gives results in rows)

print(df.isna().all(axis=1))
print(df.notna().all(axis=1))

# research
# if axis=0 what happens