import pandas as pd
import os

df = pd.read_excel("scripts/testSplit.xlsx", engine= 'openpyxl')
column_name = 'FACULTY_FULL_NAME'

value = []
for i in range(df[column_name].size):
    value = df[column_name]

df = pd.DataFrame({ 'FACULTY_FULL_NAME': value })
df[['FACULTY_ID','FACULTY_NAME']] = df.FACULTY_FULL_NAME.str.split("-", expand=True)

df.to_excel("scripts/testSplitUpdated.xlsx",
                  index = None,
                  header=True)

print(df)