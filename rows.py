
#head() tail() are used to display the first and last few rows of a DataFrame.
# They are useful for quickly inspecting the data without printing the entire DataFrame.



import pandas as pd

df=pd.read_json("sample_Data.json")

print("First 10 rows of the DataFrame:")
print(df.head(10))

print("\nLast 10 rows of the DataFrame:")
print(df.tail(10))