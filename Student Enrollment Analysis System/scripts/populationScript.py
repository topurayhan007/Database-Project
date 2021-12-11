import pandas as pd
from seas.models import School_T, Department_T, Faculty_T, Course_T, Classroom_T, Section_T

def populateDatabase(filepath):
    df = pd.read_excel(filepath, header=3, skipfooter=1, engine= 'openpyxl')
    df.to_csv ("scripts/TallySheetForAutumn2020.csv", index = None, header=True)
    df = pd.read_csv ("scripts/TallySheetForAutumn2020.csv")
    print(df)


# School Table Population
data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
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

print("School Population Successful!")


# Department Table Population
data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
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

print("Department Population Successful!")


# Course Table Population
data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
data = data[['CourseID', 'COFFERED_WITH',
             'Crs', 'COURSE_NAME', 'Dept']]
data = data.drop_duplicates()

for index, row in data.iterrows():
    Course_T(courseID=row['CourseID'],
             courseName=row['COURSE_NAME'],
             creditHour=row['Crs'],
             dept=Department_T.objects.get(deptCode=row['Dept'])).save()

print("Course Population Successful!")


# Classroom Table Population
data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
data = data[['ROOM_ID', 'RoomSize']]

data = data.drop_duplicates()
for i in range(data.shape[0]):
    Classroom_T(roomID=data.iloc[i, 0], roomCapacity=data.iloc[i, 1]).save()

print("Classroom Population Successful!")


# Faculty Table Population
data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
data = data.FACULTY_FULL_NAME.str.split('-')

data = data.drop_duplicates()

for item in data:
    try:
        Faculty_T(facultyID=item[0], facultyName=item[1]).save()
    except ValueError:
        continue

print("Faculty Population Successful!")


# Section Table Population
df = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
df2 = df.FACULTY_FULL_NAME.str.split("-")
df['FACULTY_ID'] = df2[0]
df['FACULTY_NAME'] = df2[1]
df.to_excel('scripts/Revenue_Faculty.xlsx', index = None, header=True)
print("Excel Update Success")

data = pd.read_excel('scripts/Revenue_Faculty.xlsx')

data = data[['CourseID', 'Sec', 'ROOM_ID', 'size', 'stuNo', 'Semester', 'Year', 
            'FACULTY_ID', 'STRAT_TIME', 'END_TIME', 'ST_MW', 'BLOCKED']]
# data = data.drop_duplicates()

for index, row in data.iterrows():
    Section_T(course = Course_T.objects.get(courseID = row['CourseID']),
             sectionNo = int(row['Sec']),
             room = Classroom_T.objects.get(roomID = row['ROOM_ID']),
             capacity = row['size'],
             noOfEnrolledStudent = row['stuNo'],
             semester = row['Semester'],
             year = row['Year'],
             faculty = Faculty_T.objects.get(facultyID = row['FACULTY_ID']),
            #  startTime = row['STRAT_TIME'],
            #  endTime = row['END_TIME'],
             day = row['ST_MW'],
             blocked = row['BLOCKED']).save()

print("Section Population Successful!")