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

print("DataFrame:")
print(df)


high_salary=df[df["Salary"] > 75000]
print("\nRows with Salary greater than 75000:")
print(high_salary)

# filtering rows salary>75000 and Age<35
filtered_rows=df[(df["Salary"] > 75000) & (df["Age"] < 35)]
print("\nRows with Salary greater than 75000 and Age less than 35:")
print(filtered_rows)

#using OR condition
filtered_rows_or=df[(df["Salary"] > 75000) | (df["Age"] < 30)]
print("\nRows with Salary greater than 75000 or Age less than 30:")
print(filtered_rows_or)