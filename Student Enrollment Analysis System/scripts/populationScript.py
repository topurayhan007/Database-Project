import pandas as pd
from seas.models import School_T, Department_T, Faculty_T, Course_T, Classroom_T, Section_T

def populateDatabase(filepath):
    df = pd.read_excel(filepath, header=3, skipfooter=1, engine= 'openpyxl')
    df.to_csv ("scripts/TallySheetForAutumn2020.csv", index = None, header=True)
    df = pd.read_csv ("scripts/TallySheetForAutumn2020.csv")
    print(df)

data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')

# School Table Population
data = set(data.SCHOOL_TITLE)

for item in data:
    if item == "SPPH":
        School_T(schoolTitle=item, schoolName = "School of Pharmacy and Public Health").save()
    elif item == "SLASS":
        School_T(schoolTitle=item, schoolName = "School of Liberal Arts & Social Sciences").save()
    elif item == "SETS":
        School_T(schoolTitle=item, schoolName = "School of Engineering, Technology & Sciences").save()
    elif item == "SELS":
        School_T(schoolTitle=item, schoolName = "School of Environment and Life Sciences").save()
    elif item == "SBE":
        School_T(schoolTitle=item, schoolName = "School of Business and Entrepreneurship").save()


# Department Table Population
data = data[['SCHOOL_TITLE', 'Dept']]

data = data.drop_duplicates()

for i in range(data.shape[0]):
    if data.iloc[i, 1] == "CSE":
        Department_T(deptCode=data.iloc[i, 1], deptName= "Department of Computer Science and Engineering", school=School_T.objects.get(schoolTitle=data.iloc[i, 0])).save()
    elif data.iloc[i, 1] == "EEE":
        Department_T(deptCode=data.iloc[i, 1], deptName= "Department of Electrical and Electronic Engineering", school=School_T.objects.get(schoolTitle=data.iloc[i, 0])).save()
    elif data.iloc[i, 1] == "PhySci":
        Department_T(deptCode=data.iloc[i, 1], deptName= "Department of Physical Sciences", school=School_T.objects.get(schoolTitle=data.iloc[i, 0])).save()
    else:
        Department_T(deptCode=data.iloc[i, 1], school=School_T.objects.get(schoolTitle=data.iloc[i, 0])).save()


# Course Table Population
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


# Classroom Table Population
data = data[['ROOM_ID', 'RoomSize']]

data = data.drop_duplicates()
for i in range(data.shape[0]):
    Classroom_T(roomID=data.iloc[i, 0], roomCapacity=data.iloc[i, 1]).save()

# Faculty Table Population


# Section Table Population
