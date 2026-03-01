import pandas as pd

# Read dataset
df = pd.read_csv(
    'kaggle_survey_2017_2021.csv',
    low_memory=False
)
df = df.iloc[1:].reset_index(drop=True)

df.rename(columns={'-': 'Year'}, inplace=True)

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

# 5️⃣ Select only needed columns
df = df[columns_needed]

# 6️⃣ Rename to clean names
df.columns = [
    'Year', 'Age', 'Gender',
    'Country', 'Education',
    'Job_Title', 'Experience',
    'Salary'
]

# 7️⃣ Final check
print("\nFinal Data:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())