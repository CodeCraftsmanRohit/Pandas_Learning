import pandas as pd


# read data from CSV file into a dataframe

# df=pd.read_csv("sales_data_sample.csv",encoding="latin1")
df=pd.read_excel("SampleSuperstore.xlsx")
df=pd.read_json("sample_Data.json")


print(df)

#for very large datasets, you can use the following code to read in chunks
# df=pd.read_csv("sales_data_sample.csv",encoding="latin1",chunksize=1000)
# for chunk in df:
#     print(chunk)

# if data is stored in a database, you can use the following code to read data from a SQL database
# import sqlite3
# conn = sqlite3.connect('database.db')
# df = pd.read_sql_query("SELECT * FROM sales_data", conn)
# conn.close()


# if data is stored in a google cloud DB , use gcsfs
