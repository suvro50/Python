import pandas as pd

df=pd.read_csv(r"D:\Python\Pandas\mercedesbenz.csv")

# head(n): Displays the first n rows of a DataFrame (default = 5)
# tail(n): Displays the last n rows of a DataFrame (default = 5)
print(df.head())
print(df.tail())