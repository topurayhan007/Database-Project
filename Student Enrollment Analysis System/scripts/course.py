
#importing pandas as pd
import pandas as pd
 
# Read and store content
# of an excel file
read_file = pd.read_excel ("D:/STUDY\CSE303 (Database)/Database-Project/Student Enrollment Analysis System/scripts/classSize.xlsx", engine= 'openpyxl')
 
# Write the dataframe object
# into csv file
read_file.to_csv ("D:/STUDY\CSE303 (Database)/Database-Project/Student Enrollment Analysis System/scripts/classSize.csv",
                  index = None,
                  header=True)
   
# read csv file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_csv("D:/STUDY\CSE303 (Database)/Database-Project/Student Enrollment Analysis System/scripts/classSize.csv"))
 
# show the dataframe
print(df)