import pandas as pd
import os

filepath = "scripts/testSplit.xlsx"

df = pd.read_excel(filepath, engine= 'openpyxl')
column_name = 'FACULTY_FULL_NAME'

value = []
value1 = []
for i in range(df[column_name].size):
    value = df[column_name]
    value1 = df['COURSE_NAME']

df = pd.DataFrame({ 'FACULTY_FULL_NAME': value, 'COURSE_NAME': value1})
df[['FACULTY_ID','FACULTY_NAME']] = df.FACULTY_FULL_NAME.str.split("-", expand=True)


df.to_excel("scripts/testSplitUpdated.xlsx",
                  index = None,
                  header=True)

print(df)