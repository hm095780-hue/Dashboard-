import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Iris dataset
df = sns.load_dataset("iris")

print(df.head())
mean = df['sepal_length'].mean()
median = df['sepal_length'].median()
mode = df['sepal_length'].mode()[0]

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
variance = df['sepal_length'].var()
std = df['sepal_length'].std()

print("Variance:", variance)
print("Standard Deviation:", std)
correlation = df['sepal_length'].corr(df['petal_length'])

print("Correlation:", correlation)

if correlation > 0:
    print("Relationship: Positive")
elif correlation < 0:
    print("Relationship: Negative")
else:
    print("Relationship: Weak/No relationship")

setosa_count = (df['species'] == 'setosa').sum()
total_flowers = len(df)

probability = setosa_count / total_flowers

print("Setosa flowers:", setosa_count)
print("Total flowers:", total_flowers)
print("Probability:", probability)
Q1 = df['sepal_length'].quantile(0.25)
Q3 = df['sepal_length'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df['sepal_length'] < lower_limit) |
    (df['sepal_length'] > upper_limit)
]

print("Outliers:")
print(outliers)
plt.plot(df.index, df['sepal_length'])

plt.title("Sepal Length Line Chart")
plt.xlabel("Index")
plt.ylabel("Sepal Length")

plt.show()
species_count = df['species'].value_counts()

plt.bar(species_count.index, species_count.values)

plt.title("Number of Flowers by Species")
plt.xlabel("Species")
plt.ylabel("Count")

plt.show()
plt.pie(
    species_count.values,
    labels=species_count.index,
    autopct='%1.1f%%'
)

plt.title("Flower Species Distribution")

plt.show()
plt.hist(df['sepal_length'], bins=10)

plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")

plt.show()
plt.scatter(
    df['sepal_length'],
    df['petal_length']
)

plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")

plt.show()
sns.countplot(data=df, x='species')

plt.title("Count of Flowers by Species")
plt.xlabel("Species")
plt.ylabel("Count")

plt.show()
sns.boxplot(
    data=df,
    x='species',
    y='sepal_length'
)

plt.title("Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length")

plt.show()
correlation_matrix = df.select_dtypes(
    include='number'
).corr()

sns.heatmap(
    correlation_matrix,
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()
sns.pairplot(
    df,
    hue='species'
)

plt.show()
print("Rows and Columns:", df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())
print(df.isnull().sum())
df['sepal_length'] = df['sepal_length'].fillna(
    df['sepal_length'].median()
)

df['sepal_width'] = df['sepal_width'].fillna(
    df['sepal_width'].median()
)

df['petal_length'] = df['petal_length'].fillna(
    df['petal_length'].median()
)

df['petal_width'] = df['petal_width'].fillna(
    df['petal_width'].median()
)

df['species'] = df['species'].fillna(
    df['species'].mode()[0]
)
print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

print("After removing duplicates:", df.shape)
print(df.describe())
print(df['species'].unique())
print("Before Cleaning")
print(df.head())
print(df.shape)
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print("After Cleaning")
print(df.head())
print(df.shape)
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
corr = df.select_dtypes(include='number').corr()

print(corr)
plt.figure(figsize=(8, 5))

sns.heatmap(
    corr,
    annot=True
)

plt.title("Correlation Between Numerical Variables")

plt.show()