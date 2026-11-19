# info() → Provides a summary of a DataFrame,
#  including column names, non-null values, data types, number of rows and columns, and memory usage.

import pandas as pd

data=pd.read_csv(r"D:\Python\Pandas\mercedesbenz.csv")

print(data.info())