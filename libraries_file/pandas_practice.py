import pandas as pd
import numpy as np

# Load your dataset
df=pd.read_csv('libraries_file\passenger_data.csv')


# Add Titanic-like columns

# Add random Survived column (0 = not survived, 1 = survived)
df["Survived"] = np.random.randint(0, 2, size=len(df))

df["Pclass"] = np.random.choice([1, 2, 3], size=len(df))

df["Embarked"] = np.random.choice(["C", "Q", "S"], size=len(df))

# Create random sibsp (0 to 3 siblings/spouses)
df["SibSp"] = np.random.randint(0, 4, size=len(df))

# Create random parch (0 to 2 parents/children)
df["Parch"] = np.random.randint(0, 3, size=len(df))


# Save new dataset
df.to_csv("libraries_file\passenger_titanic_style.csv", index=False)
print("✅ Dataset updated and saved as passenger_titanic_style.csv")

print(df.columns)

print("----------Question-1----------")
# Show the first 10 rows of the dataset.
print(df.head(10))


print("----------Question-2----------")
# What are the column names, shape, and datatypes of the dataset?

print(df.columns)
print(df.shape)
print(df.dtypes)


print("----------Question-3----------")
# How many missing values are there in each column?

missing_values = df.isnull().sum()
print(missing_values)


print("----------Question-4----------")
# Find the number of passengers who survived and who didn’t.

survival_counts = df["Survived"].value_counts()
print(survival_counts)


print("----------Question-5----------")
# Find the percentage of passengers who survived.

survival_percentage = (df["Survived"].mean()) * 100
print(survival_percentage)


print("----------Question-6----------")
# What is the average age of the passengers?

print(df['Age'].mean())


print("----------Question-7----------")
# Find the maximum and minimum fares paid.

print(df['Fare'].min())
print(df['Fare'].max())


print("----------Question-8----------")
# How many passengers were male vs female?

print(df["Gender"].value_counts())


print("----------Question-9----------")
# How many passengers embarked from each port? (C, Q, S)

embarked_counts = df["Embarked"].value_counts()
print(embarked_counts)


print("----------Question-9----------")
# Find the most common passenger age.

print(df["Age"].mode()[0])


print("----------Question-10----------")
# How many unique ticket classes (pclass) are there?

unique_classes = df["Pclass"].nunique()
print("Number of unique ticket classes:", unique_classes)


print("----------Question-11----------")
# What is the average age of survivors vs non-survivors?

avg_age = df.groupby("Survived")["Age"].mean()
print(avg_age)


print("----------Question-12----------")
# What is the survival rate by gender?

survival_by_gender = df.groupby("Gender")["Survived"].mean()
print(survival_by_gender)


print("----------Question-13----------")
# What is the survival rate by passenger class (pclass)?

survival_rate = df.groupby("Pclass")["Survived"].mean()
print(survival_rate)


print("----------Question-14----------")
# What is the average fare paid by each class?

avg_fare=df.groupby("Pclass")["Fare"].mean()
print(avg_fare)


print("----------Question-15----------")
# Which age group had the highest survival rate? (e.g., children vs adults vs seniors).

df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 12, 18, 60, 100], labels=["Children", "Teens", "Adults", "Seniors"])
high_surv_rate=df.groupby("AgeGroup")["Survived"].mean()
print(high_surv_rate)


print("----------Question-16----------")
# How many passengers traveled with siblings/spouses (sibsp) vs alone?

sib=df["SibSp"].value_counts()
print(sib)


print("----------Question-17----------")
# Find the most common passenger age.

com_pass_age=df["Age"].mode()[0]
print(com_pass_age)


print("----------Question-18----------")
# What is the average fare paid by survivors vs non-survivors?

avg_fare1=df.groupby("Survived")["Fare"].mean()
print(avg_fare1)


print("----------Question-19----------")
# Compare survival rates by family size.

df["Family_Size"] = df["SibSp"] + df["Parch"] + 1

sur_rate_by_size = df.groupby("Family_Size")["Survived"].mean()
print(sur_rate_by_size)


print("----------Question-20----------")
# Create a new column "family_size" = sibsp + parch + 1. how to create this

df["Family_size"] = df["SibSp"] + df["Parch"] + 1
print(df)
