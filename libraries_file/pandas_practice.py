import pandas as pd
import numpy as np

df=pd.read_csv('libraries_file\passenger_data.csv')
print(df)

print("----------Question-1----------")
# Show the first 10 rows of the dataset.
print(df.head(10))

print("----------Question-2----------")
# What are the column names, shape, and datatypes of the dataset?

print(df.columns)
print(df.shape)
print(df.dtypes)

print("----------Question-3----------")
# What is the average age of the passengers?

print(df['Age'].mean())

print("----------Question-4----------")
# Find the maximum and minimum fares paid.

print(df['Fare'].min())
print(df['Fare'].max())

print("----------Question-5----------")
# How many passengers were male vs female?

print(df["Gender"].value_counts())

print("----------Question-6----------")
# Find the most common passenger age.

print(df["Age"].mode()[0])


print("----------Question-7----------")
# Create a new column "family_size" = sibsp + parch + 1. how to create this

# In this data set, I dont have sibsp and parch columns so that why I created these two cols using numpy as shown below

# Create random sibsp (0 to 3 siblings/spouses)
df["sibsp"] = np.random.randint(0, 4, size=len(df))

# Create random parch (0 to 2 parents/children)
df["parch"] = np.random.randint(0, 3, size=len(df))

# Create family_size column
df["family_size"] = df["sibsp"] + df["parch"] + 1

print(df)


print("----------Question-8----------")
# What is the survival rate by gender?'

# In this data set, I dont have sibsp and parch columns so that why I created these two cols using numpy as shown below

# Add random Survived column (0 = not survived, 1 = survived)
df["Survived"] = np.random.randint(0, 2, size=len(df))

# Calculate survival rate by gender
survival_rate = df.groupby("Gender")["Survived"].mean()
print(survival_rate)










# How many missing values are there in each column?
