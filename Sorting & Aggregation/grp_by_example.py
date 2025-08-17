import pandas as pd



data={
    "Name":['Arun','Varun','Karun','Narun','Marun'],
    "Age":[28,34,22,34,28],
    "Salary":[10000,20000,30000,40000,50000]

}

df=pd.DataFrame(data)

# grouped=df.groupby("Age")["Salary"].sum()
# print(grouped)

grouped=df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)
