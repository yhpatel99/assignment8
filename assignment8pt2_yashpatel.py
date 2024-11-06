import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Loan Dataset
loan_df = pd.read_csv('loan_data.csv')

# Data Visualization 1: Distribution of Loan Amounts
plt.figure(figsize=(10, 6))
sns.histplot(loan_df['loan_amnt'], kde=True, bins=30, color='blue')
plt.title('Distribution of Loan Amounts')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.show()

# Data Visualization 2: Loan Amount by Current Loan Status
plt.figure(figsize=(10, 6))
sns.boxplot(data=loan_df, x='Current_loan_status', y='loan_amnt', palette='viridis')
plt.title('Loan Amount by Current Loan Status')
plt.xlabel('Current Loan Status')
plt.ylabel('Loan Amount')
plt.xticks(rotation=45)
plt.show()

# Data Visualization 3: Interest Rate by Loan Grade
plt.figure(figsize=(10, 6))
sns.boxplot(data=loan_df, x='loan_grade', y='loan_int_rate', palette='viridis')
plt.title('Interest Rate by Loan Grade')
plt.xlabel('Loan Grade')
plt.ylabel('Interest Rate')
plt.show()

# Analysis
analysis = """
Based on the visualizations:
1. The distribution of loan amounts shows that most loans are within a certain range.
2. The box plot of loan amounts by current loan status shows that certain loan have higher loan amounts.
3. The box plot of interest rates by loan grade shows that higher grades are with lower interest rates.
"""
print(analysis)