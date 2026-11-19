#Filter Columns:
# Series-> Select Single Column 
# DataFrame -> Select multiple columns

import pandas as pd

# Create Dictionary ={ "key": [value] }
data={
    "Name":["Suvrojit","Dip","Sudipto","Raju","Kajol","Adi","Ram","Shyam"],
    "Age":[21,18,20,23,25,30,32,35],
    "Salary":[50000,40000,35000,30000,32000,37000,25000,23000],
    "Performance Score":[92,80,81,70,73,75,78,83]
}

df=pd.DataFrame(data)
print(df) 

print(df["Name"]) # Series
print(df[["Name","Age"]]) # DataFrame



# Filer Rows
print("Filter Single Row: ")
print(df[df["Age"] > 20]) # Filter single row

print("Filter Multiple row: ")
print(df[ (df["Age"] > 20) & (df["Salary"] > 30000)]) # Filter Multiple row

print("Multiple row with OR:")
print(df[(df["Age"] > 20) | (df["Salary"] > 30000)])
