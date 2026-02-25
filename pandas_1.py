import pandas as pd

data = {
    'Name': ['Alice', 'Goud', 'Charlie','Naresh'],
    'Age': [25, 30, 35,33],
    'City': ['New York', 'Hyderabad', 'Paris','Hyderabad']
}

s=pd.Series(data)

df = pd.DataFrame(data)
df.head()  # Display the first few rows of the DataFrame
print(df.groupby('City').size())

# Group by 'City' and calculate the mean age for each city
mean_age_by_city = df.groupby('City')['Age'].mean()

print(mean_age_by_city)
