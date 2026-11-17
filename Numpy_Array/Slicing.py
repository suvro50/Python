import numpy as np

arr=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
# arr[start:end:step]  -> ending index is exclusive
# arr[row_start:row_end:row_step, column_start:column_end:column_step]
print(arr[0:3])
print(arr[0:4]) # print all , because take extra index
# another way to print all--> print(arr[0:])

# Row selection
print("Row selection:\n",arr[0::3])
print("Row selection:\n",arr[::-2]) # from last

# column selection  arr[:, start:end:step]
print("column selection:\n",arr[:,0:2 ])

# select row , and column both 
print("Row:1 and column:1\n",arr[0:2 , 0:2]) # first quater
print("2nd quater: \n",arr[0:2 , 2:4])