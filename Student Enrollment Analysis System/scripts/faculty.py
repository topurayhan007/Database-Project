import pandas as pd
from seas.models import Faculty_T

df = pd.read_excel("scripts/Revenue.xlsx", sheet_name='Data')
df2 = df.FACULTY_FULL_NAME.str.split("-", expand=True)
df['FACULTY_ID'] = df2[0]
df['FACULTY_NAME'] = df2[1]
df.to_excel("scripts/Revenue.xlsx", index = None, header=True)
print(df)

# for i in range(data.shape[0]):
#     Faculty_T(facultyID=data.iloc[i, 11], facultyName=data.iloc[i, 12]).save()

