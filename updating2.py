import pandas as pd

data={
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Salary': [70000, 80000, 90000],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Department': ['HR', 'Engineering', 'Marketing'],
    'Joining Date': ['2020-01-15', '2019-03-22', '2021-07-30'],
    'Performance Score': [4.5, 3.8, 4.2],
}

df=pd.DataFrame(data)



print(df)
df['Salary']=df['Salary']*1.05
print(df)