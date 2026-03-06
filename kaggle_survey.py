import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt


# Read dataset
df = pd.read_csv(
    'kaggle_survey_2017_2021.csv',
    low_memory=False
)
df = df.iloc[1:].reset_index(drop=True)

df.rename(columns={'-': 'Year'}, inplace=True)

#cleaning data
print("Columns after rename:")
print(df.columns[:10])

print("\nColumns containing Q25 or Q24:")
for col in df.columns:
    if "Q25" in col or "Q24" in col:
        print(col)

columns_needed = [
    'Year', 'Q1', 'Q2', 'Q3',
    'Q4', 'Q5', 'Q6', 'Q25'
]

df = df[columns_needed]

df.columns = [
    'Year', 'Age', 'Gender',
    'Country', 'Education',
    'Job_Title', 'Experience',
    'Salary'
]

print("\nFinal Data:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())

#Salary cleaning
def clean_salary(value):
    if pd.isna(value):
        return np.nan
    value = value.replace('$', '')
    value = value.replace(',', '')
    numbers = re.findall(r'\d+', value)
    if len(numbers) == 2:
        low = int(numbers[0])
        high = int(numbers[1])
        return (low + high) / 2
    
    return np.nan

df['Salary_Numeric'] = df['Salary'].apply(clean_salary)

print(df[['Salary', 'Salary_Numeric']].head())

df = df.dropna(subset=['Salary_Numeric'])

df['Experience'] = df['Experience'].fillna('Unknown')
df['Job_Title'] = df['Job_Title'].fillna('Unknown')
df['Education'] = df['Education'].fillna('Unknown')
df['Country'] = df['Country'].fillna('Unknown')
df['Gender'] = df['Gender'].fillna('Unknown')

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Insight
#Highest paying jobs
salary_by_job = df.groupby('Job_Title')['Salary_Numeric'].mean().sort_values(ascending=False)

print("\nTop 10 Highest Paying Jobs:")
print(salary_by_job.head(10))


# ----------------------------

#Salary by experience
salary_by_exp = df.groupby('Experience')['Salary_Numeric'].mean().sort_values(ascending=False)

print("\nAverage Salary by Experience:")
print(salary_by_exp)

# ----------------------------

#Salary by country
salary_by_country = df.groupby('Country')['Salary_Numeric'].mean().sort_values(ascending=False)

print("\nTop 10 Countries by Salary:")
print(salary_by_country.head(10))

#visualization
#Top Jobs
top_jobs = salary_by_job.head(5)
plt.figure(figsize=(10,6))

top_jobs.plot(kind='bar')

plt.title("Top 5 Highest Paying Data Science Jobs", fontsize=14)
plt.xlabel("Job Title")
plt.ylabel("Average Salary ($)")
plt.xticks(rotation=25)

plt.tight_layout()
plt.show()

#Experience vs Salary
plt.figure(figsize=(12,6))

order = [
    '< 1 year',
    '1-3 years',
    '3-5 years',
    '5-10 years',
    '10-20 years',
    '20+ years'
]

exp_salary = df.groupby("Experience")["Salary_Numeric"].mean().reindex(order)

exp_salary.plot(kind='bar')

plt.title("Average Salary by Experience Level", fontsize=14)
plt.xlabel("Experience Level")
plt.ylabel("Average Salary ($)")
plt.xticks(rotation=30)

plt.tight_layout()
plt.show()

# Top 10 Countries by Salary
top_countries = df.groupby("Country")["Salary_Numeric"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))

top_countries.plot(kind='barh')

plt.title("Top 10 Countries by Average Data Science Salary", fontsize=14)
plt.xlabel("Average Salary ($)")
plt.ylabel("Country")

plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()