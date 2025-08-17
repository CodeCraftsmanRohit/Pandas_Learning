import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Salary': [70000, 80000, 90000],
    'Department': ['HR', 'Engineering', 'Marketing'],
    'Joining Date': ['2020-01-15', '2019-03-22', '2021-07-30'],
    'Performance_Score': [4.5, 3.8, 4.2],
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Remove column
df.drop(columns=['Performance_Score'], inplace=True)

print("\nModified DataFrame:")
print(df)
