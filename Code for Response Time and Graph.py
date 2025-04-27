import pandas as pd
import matplotlib.pyplot as plt

#Load the Excel file
df = pd.read_excel('Incident Data.xlsx')

#Convert times to datetime format
df['Reported Time'] = pd.to_datetime(df['Reported Time'])
df['Resolved Time'] = pd.to_datetime(df['Resolved Time'])

#Calculate Response Time (in hours)
df['Response Time (Hours)'] = (df['Resolved Time'] - df['Reported Time']).dt.total_seconds() / 3600

#Group by Priority and find average response time
avg_response_time = df.groupby('Priority')['Response Time (Hours)'].mean()

print(avg_response_time)

#Plot the average response time
avg_response_time.plot(kind='bar', color='skyblue')
plt.title('Average Response Time by Priority')
plt.xlabel('Priority')
plt.ylabel('Average Response Time (Hours)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

