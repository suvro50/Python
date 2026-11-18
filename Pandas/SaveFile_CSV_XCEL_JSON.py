
import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam'],
    "Age": [10, 20, 30],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data) #converting a Python dictionary into a Pandas DataFrame (table)

print(df)

#df.to_csv("D:\Python\Pandas\output.csv", index=False)
#df.to_excel("D:\Python\Pandas\output.xlsx", index=False)
df.to_json("D:\Python\Pandas\output.json", index=False)
