from numpy import NaN, nan
import pandas as pd
from seas.models import Faculty_T

df = pd.read_excel("scripts/Revenue.xlsx", skiprows=[1,1021], sheet_name='Data')
df2 = df.FACULTY_FULL_NAME.str.split("-", expand=True)
df['FACULTY_ID'] = df2[0]
df['FACULTY_NAME'] = df2[1]

print('Pushing in dataframe')
df = df[['FACULTY_ID', 'FACULTY_NAME']]
# Removing all FACULTY_NAME with "00 TBA TBA" to "TBA"
for i in range(df.shape[0]):
    if df.iloc[i, 1] == "00 TBA TBA":
        df.iloc[i, 1] = "TBA"
        print(df.iloc[i, 1])
# Removing all FACULTY_ID with "T100" to "0"
for i in range(df.shape[0]):
    if df.iloc[i, 0] == "T001":
        df.iloc[i, 0] = 0
        print(df.iloc[i, 0])
# Removing a FACULTY_ID with "V011" to "0000"
for i in range(df.shape[0]):
    if df.iloc[i, 0] == "V011":
        df.iloc[i, 0] = 0000
        print(df.iloc[i, 0])
        
    
df.to_excel("scripts/Revenue_Faculty.xlsx", index = None, header=True)
print(df)

data = pd.read_excel("scripts/Revenue_Faculty.xlsx")
data = data[['FACULTY_ID', 'FACULTY_NAME']]
data = data.drop_duplicates()

print("Starting Population.........")
for item in data:
    print(item)

for i in range(data.shape[0]):
    print(data.iloc[i,0])
    Faculty_T(facultyID=data.iloc[i, 0], facultyName=data.iloc[i, 1]).save()

print('Success! populating')

# for index, row in data.iterrows():
#     if type(row['FACULTY_ID']) != int:
#         Faculty_T(facultyID=0, facultyName="TBA").save()
#     elif type(row['FACULTY_ID']) == str:
#         Faculty_T(facultyID=row['FACULTY_ID'], facultyName=row['FACULTY_NAME']).save()
