# df["Column Name"].mean()
# df["Column Name"].sum()
# df["Column Name"].min()


import pandas as pd

data={
    "Name":['Arun','Varun','Karun'],
    "Age":[28,34,22],
    "Salary":[10000,20000,30000]

}

df=pd.DataFrame(data)

avr_salary=df['Salary'].mean()
print(avr_salary)