# Pandas is a powerful Python library.
# Pandas used for Data Analysis and Data Manipulation.
# V.V.I:
# **Why Use Pandas?**
# 1.Performance: Handles millions of rows efficiently.
# 2.Ease of Use: Beginner-friendly syntax for cleaning and transforming data.
# 3.Integration: Works with libraries like Matplotlib (visualizations) and Scikit-learn (Machine Learning).
# install pandas = pip install pandas
import pandas as pd

# Series = A series is an one dimensional labeled array that can hold any data type :integers,floats,
#         strings, or even python objects. Each element in the Series has a unique label called an index

# Series is used to track changes or patterns over time, such as daily temperatures, stock price, or sales revenue


# Read data from CSV file into a dataframe
# if get error data read time, than use : encoding="utf-8" or encoding="latin1"
# Example: r"D:\python\Pandas\mercedesbenz.csv,encoding="latin1" "
data=pd.read_csv(r"D:\python\Pandas\mercedesbenz.csv")
print(data)