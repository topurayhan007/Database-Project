import pandas as pd
from seas.models import Department_T, School_T

data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
data = data[['SCHOOL_TITLE', 'CourseID']]

for i in range(data.shape[0]):
    data.iloc[i, 1] = data.iloc[i, 1][:3]

data = data.drop_duplicates()

for i in range(data.shape[0]):
    Department_T(deptCode=data.iloc[i, 1], school=School_T.objects.get(schoolTitle=data.iloc[i, 0])).save()
