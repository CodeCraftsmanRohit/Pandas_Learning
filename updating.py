import pandas as pd

data={
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Salary': [70000, 80000, 90000],
    'Department': ['HR', 'Engineering', 'Marketing'],
    'Joining Date': ['2020-01-15', '2019-03-22', '2021-07-30'],
    'Performance Score': [4.5, 3.8, 4.2],
}

df=pd.DataFrame(data)


# .loc[]
# df.loc[row_index,"Column Name"]=new_value
df.loc[0,'Salary']=55000
print(df)