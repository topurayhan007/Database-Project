import pandas as pd
import os

filepath = "scripts/testSplit.xlsx"

df = pd.read_excel(filepath, engine= 'openpyxl')
column_name = 'FACULTY_FULL_NAME'

value = []
value1 = []
for i in range(df[column_name].size):
    value1 = df[column_name]
    value = df['COURSE_NAME']

df = pd.DataFrame({ 'COURSE_NAME': value, 'FACULTY_FULL_NAME': value1})
df2 = df.FACULTY_FULL_NAME.str.split("-", expand=True)

df['FACULTY_ID'] = df2[0]
df['FACULTY_NAME'] = df2[1]

df.to_excel("scripts/testSplit.xlsx",
                  index = None,
                  header=True)

print(df)