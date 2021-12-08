import pandas as pd
from seas.models import Course_T, Department_T

data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
data = data[['CourseID', 'COFFERED_WITH',
             'Crs', 'COURSE_NAME', 'Year', 'Semester']]
data = data.drop_duplicates()

for index, row in data.iterrows():
    Course_T(courseID=row['CourseID'],
             courseName=row['COURSE_NAME'],
             creditHour=row['Crs'],
             semester=row['Semester'],
             year=row['Year'],
             dept=Department_T.objects.get(deptCode=row['CourseID'][:3])).save()
