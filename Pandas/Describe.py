# This is very very powerfull function
# describe() → Generates a statistical summary of numerical columns, 
# including count, mean, standard deviation, minimum, maximum, and quartiles.
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

print("Describe Statistic: ")
print(df.describe())   #If all column not show than use: df.describe().to_string()



# V.V.I: 
# count: Number of non-empty values.
# mean: Average value.
# std: Standard deviation (measures how spread out the values are).
# min: Minimum (smallest) value.
# 25%: First quartile (25% of values are at or below this value).
# 50%: Median (middle value).
# 75%: Third quartile (75% of values are at or below this value).
# max: Maximum (largest) value.