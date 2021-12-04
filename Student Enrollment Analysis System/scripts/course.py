#importing pandas as pd
import pandas as pd
from pandas import read_csv, read_excel, to_csv
 
# Read and store content
# of an excel file
read_file = pd.read_excel("scripts/classSize.xlsx", engine= 'openpyxl')
 
# Write the dataframe object
# into csv file
read_file.to_csv ("scripts/classSize.csv",
                  index = None,
                  header=True)
   
# read csv file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_csv("scripts/classSize.csv"))
 
# show the dataframe
print(df)