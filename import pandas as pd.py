import pandas as pd
data=pd.read_csv('/path/file_name.csv')
print(data.head())

data=pd.read_csv('/path/file.csv',sep='|')