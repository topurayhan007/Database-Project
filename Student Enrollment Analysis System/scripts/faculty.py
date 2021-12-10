from numpy import NaN, nan
import pandas as pd
from seas.models import Faculty_T

df = pd.read_excel("scripts/Revenue.xlsx", sheet_name='Data')
df2 = df.FACULTY_FULL_NAME.str.split("-", expand=True)
df['FACULTY_ID'] = df2[0]
df['FACULTY_NAME'] = df2[1]
for i in df['FACULTY_ID']:
    if i == "T001":
        i = 0
    
df.to_excel("scripts/Revenue_Faculty.xlsx", index = None, header=True)
print(df)

data = pd.read_excel("scripts/Revenue_Faculty.xlsx")
data = data[['FACULTY_ID', 'FACULTY_NAME']]
data = data.drop_duplicates()

# for index, row in data.iterrows():
#     if type(row['FACULTY_ID']) != int:
#         Faculty_T(facultyID=0, facultyName="TBA").save()
#     elif type(row['FACULTY_ID']) == str:
#         Faculty_T(facultyID=row['FACULTY_ID'], facultyName=row['FACULTY_NAME']).save()


for i in range(data.shape[0]):
    Faculty_T(facultyID=data.iloc[i, 0], facultyName=data.iloc[i, 1]).save()
