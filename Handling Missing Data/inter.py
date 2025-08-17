
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, None, 35],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Salary': [None, 80000, 90000],
    'Department': ['HR', 'Engineering', 'Marketing'],
    'Joining Date': ['2020-01-15', '2019-03-22', '2021-07-30'],
    'Performance_Score': [4.5, 3.8, None],
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# linear,polynomial,time

df=df.interpolate(method="linear",axis=0)
print(df)