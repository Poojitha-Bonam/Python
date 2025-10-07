import pandas as pd
import matplotlib.pyplot as plt

# Q2. Load the file using pandas
df = pd.read_csv("libraries_file\population.csv")
print(df)

# Q3. Plot India’s population over time
plt.figure(figsize=(6,4))
plt.plot(df["Year"], df["India"], marker='o', color='orange')
plt.title("India's Population Over Time")
plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.grid(True)
plt.show()

# Q4. Plot both India and China on the same graph
plt.figure(figsize=(6,4))
plt.plot(df["Year"], df["India"], marker='o', label="India")
plt.plot(df["Year"], df["China"], marker='s', label="China")
plt.title("India vs China Population Over Time")
plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.legend()
plt.grid(True)
plt.show()

# Q5. Bar chart comparing India, China, USA, Brazil for 2020
data_2020 = df[df["Year"] == 2020].iloc[0, 1:]
countries = data_2020.index
values = data_2020.values

plt.figure(figsize=(6,4))
plt.bar(countries, values, color=['orange', 'red', 'blue', 'green'])
plt.title("Population Comparison (2020)")
plt.xlabel("Country")
plt.ylabel("Population (millions)")
plt.grid(True, axis='y')
plt.show()

# Q6. Pie chart showing each country’s percentage of total population in 2020
plt.figure(figsize=(5,5))
plt.pie(values, labels=countries, autopct='%1.1f%%', startangle=140)
plt.title("Population Share (2020)")
plt.show()

# Q8. Create a 2x2 figure layout
fig, axes = plt.subplots(2, 2, figsize=(10,8))

# (Top-left) → Line plot of India
axes[0,0].plot(df["Year"], df["India"], marker='o', color='orange')
axes[0,0].set_title("India's Population Over Time")
axes[0,0].set_xlabel("Year")
axes[0,0].set_ylabel("Population (millions)")
axes[0,0].grid(True)

# (Top-right) → Bar chart (2020 comparison)
axes[0,1].bar(countries, values, color=['orange','red','blue','green'])
axes[0,1].set_title("Population Comparison (2020)")
axes[0,1].set_xlabel("Country")
axes[0,1].set_ylabel("Population (millions)")
axes[0,1].grid(True, axis='y')

# (Bottom-left) → Pie chart (2020 share)
axes[1,0].pie(values, labels=countries, autopct='%1.1f%%', startangle=140)
axes[1,0].set_title("Population Share (2020)")

# (Bottom-right) → Any other graph (let's use USA vs Brazil line plot)
axes[1,1].plot(df["Year"], df["USA"], marker='^', label="USA")
axes[1,1].plot(df["Year"], df["Brazil"], marker='s', label="Brazil")
axes[1,1].set_title("USA vs Brazil Population Over Time")
axes[1,1].set_xlabel("Year")
axes[1,1].set_ylabel("Population (millions)")
axes[1,1].legend()
axes[1,1].grid(True)

plt.tight_layout()
plt.show()