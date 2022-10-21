import pandas as pd

df = pd.read_csv(r'./test_metadata.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
print(df)