import pandas as pd
# import numpy as np
df=pd.read_csv('budget_data.csv')
# print(df.head())
# print(df.info())    

df['Date'] =pd.to_datetime(df['Date'], format="%d/%m/%Y", errors='coerce')
# dfnew=df.dropna()
# print(df.head())
print(df)
# print(df.info())   

# Goals:

# Total money spent

# Number of transactions

# Number of unique items

# Spending per category 

total_spent = df['Amount'].sum()
num_transactions = df['Amount'].count()
num_unique_items = df['Item'].nunique()
spending_per_category = df.groupby('Category')['Amount'].sum()
print("Total money spent:", total_spent)
print("Number of transactions:", num_transactions)
print("Number of unique items:", num_unique_items)
print("Spending per category:")
print(spending_per_category)