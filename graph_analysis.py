import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df=pd.read_csv('budget_data.csv')
df['Date'] =pd.to_datetime(df['Date'], format="%d/%m/%Y", errors='coerce')
# print(df.head())
# daily_transaction = df.groupby(df['Date'].dt.date)['Amount'].count()
# print(daily_transaction)
# daily_spend = df.groupby(df['Date'].dt.date)['Amount'].sum()

# daily_transaction.plot(kind='line', figsize=(10,5), title='Daily Transactions')
# plt.show()
# daily_spend.plot(kind='line', figsize=(10,5), title='Daily Spending')
# plt.show()


# weekly transaction
# Weekly trend
# df['day'] = df['Date'].dt.day_name()
# sns.barplot(x='day', y='Amount', data=df, estimator=sum)
# plt.title("Spending by Day of Week")
# plt.show()

# sns.barplot(x='Date',y='Amount', data=df, estimator=sum)
# plt.title("Spending by Date")
# plt.show()

# show spending per week but show x labels week 1 week 2
df['week'] = df['Date'].dt.to_period('W').apply(lambda r: r.start_time)
sns.barplot(x='week', y='Amount', data=df, estimator=sum)
plt.title("Spending by Week")
plt.show()
# show spending per month
# df['month'] = df['Date'].dt.to_period('M').apply(lambda r: r.start_time)
# sns.barplot(x='month', y='Amount', data=df, estimator=sum)
# plt.title("Spending by Month")
# plt.show()

# sns.barplot(x='Category', y='Amount', data=df, estimator=sum)
# plt.title("Spending by Category")
# plt.show()
