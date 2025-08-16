'''
1- how big is yor dataset
2- what are the names of columns
3- what is the data type of each column
4- what is the shape of the dataset


'''
import pandas as pd

data={
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Salary': [70000, 80000, 90000],
    'Is_Employed': [True, True, False],
}

df=pd.DataFrame(data)

print(df)

print('Dataset Size:', df.size)
print('Column Names:', df.columns.tolist())
print('Data Types:', df.dtypes.to_dict())
print('Shape of Dataset:', df.shape)

print(f'Dataset Size: {df.shape[0]} rows and {df.shape[1]} columns')