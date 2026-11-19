# shape → Returns the number of rows and columns in a DataFrame.
# columns → Returns the names of all columns in a DataFrame.

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

print(f"Shape: {df.shape}") #  show (Row,Columns)
print(f"Columns: {df.columns}")