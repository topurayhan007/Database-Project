import pandas as pd
from seas.models import Department_T, School_T

data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
data = data[['SCHOOL_TITLE', 'CourseID']]

for i in range(data.shape[0]):
    data.iloc[i, 1] = data.iloc[i, 1][:3]

data = data.drop_duplicates()

for i in range(data.shape[0]):
    if i == "CSE":
        Department_T(deptCode=data.iloc[i, 1], deptName= "Department of Computer Science and Engineering", school=School_T.objects.get(schoolTitle=data.iloc[i, 0])).save()
    elif i == "EEE":
        Department_T(deptCode=data.iloc[i, 1], deptName= "Department of Electrical and Electronic Engineering", school=School_T.objects.get(schoolTitle=data.iloc[i, 0])).save()
    elif i == "PS":
        Department_T(deptCode=data.iloc[i, 1], deptName= "Department of Physical Sciences", school=School_T.objects.get(schoolTitle=data.iloc[i, 0])).save()
    else:
        Department_T(deptCode=data.iloc[i, 1], school=School_T.objects.get(schoolTitle=data.iloc[i, 0])).save()


