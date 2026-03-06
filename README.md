📊 Kaggle Data Science Survey Analysis (2017–2021)

An end-to-end Data Cleaning and Insight Generation project based on the Kaggle Machine Learning & Data Science Survey dataset (2017–2021).

This project focuses on transforming messy real-world survey data into meaningful insights about data science careers, salaries, experience levels, and global trends.

📌 Project Objective

The goal of this project is to simulate a real-world data analyst workflow, including:

Cleaning messy survey data

Handling missing values

Transforming categorical variables

Converting salary ranges into numeric values

Generating insights about the global data science job market

Visualizing key findings

📂 Dataset

Source: Kaggle Machine Learning & Data Science Survey

The dataset includes responses from thousands of data professionals worldwide about:

Age

Gender

Country

Education

Job title

Programming experience

Salary

🛠 Tools & Technologies

Python

Pandas

NumPy

Matplotlib

Data Cleaning

Exploratory Data Analysis (EDA)

🧹 Data Cleaning Process

The dataset required several preprocessing steps:

✔ Renamed unclear columns (Q1, Q2, etc.)
✔ Selected the most relevant features
✔ Handled missing values
✔ Standardized categorical variables
✔ Converted salary ranges → numeric values
✔ Removed inconsistent entries

Example:

Salary Range → Numeric Salary

25,000-29,999 → 27,499
60,000-69,999 → 64,999
$0-999 → 499

After cleaning:

Missing values before cleaning:
Salary: 47,499
Experience: 13,516
Job Title: 7,214

Missing values after cleaning:
0
📊 Key Insights
1️⃣ Highest Paying Data Roles

Top roles with the highest average salaries:

Product Manager

Chief Officer

Project Manager

Program Manager

Principal Investigator

These roles combine technical expertise with leadership responsibilities, which significantly increases compensation.

2️⃣ Experience vs Salary

Salary increases significantly with experience.

Key observation:

Entry level (<1 year): ~20K

Mid-level (5–10 years): ~54K

Senior professionals (20+ years): ~89K

This highlights the strong correlation between experience and salary growth in data-related fields.

3️⃣ Top Countries by Data Science Salary

Countries with the highest average salaries:

1️⃣ United States
2️⃣ Switzerland
3️⃣ Australia

These countries lead the global data science job market in terms of compensation.

📈 Visualizations

The project includes several charts:

Top Paying Jobs

Shows the highest paying roles in the data industry.

Salary by Experience

Demonstrates how compensation increases with professional experience.

Top Countries by Salary

Highlights global salary distribution across countries.

🚀 What This Project Demonstrates

This project highlights core Data Analyst skills, including:

✔ Data Cleaning
✔ Feature Engineering
✔ Exploratory Data Analysis
✔ Insight Generation
✔ Data Visualization
