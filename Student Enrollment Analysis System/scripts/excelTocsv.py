#importing pandas as pd
import pandas as pd
 
# Read and store content of an excel file
# read_file = pd.read_excel("scripts/TallySheetForAutumn2020.xlsx", engine= 'openpyxl')

# Use this code to read from TallySheet
read_file = pd.read_excel("scripts/TallySheetForSpring2021.xlsx", engine= 'openpyxl')
 
# Write the dataframe object into csv file
read_file.to_csv ("scripts/TallySheetForSpring2021.csv",
                  index = None,
                  header=True)
   
# read csv file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_csv("scripts/TallySheetForSpring2021.csv"))
 
# show the dataframe
print(df)