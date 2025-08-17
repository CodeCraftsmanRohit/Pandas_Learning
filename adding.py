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


df["Bonus"] =df["Salary"]*0.1
print(df)

#using insert()
# df.insert(loc,"Column_Name",some_data)
df.insert(0,"Employee ID",[10,20,30])
print(df)