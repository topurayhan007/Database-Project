# class Section_T(models.Model):
#     course = models.ForeignKey(Course_T, on_delete=CASCADE)
#     sectionNo = models.IntegerField(primary_key=True)
#     room = models.ForeignKey(Classroom_T, on_delete=CASCADE)
#     capacity = models.IntegerField()
#     noOfEnrolledStudent = models.IntegerField()
#     faculty = models.ForeignKey(Faculty_T, on_delete=CASCADE)
#     startTime = models.TimeField()
#     endTime = models.TimeField()
#     day = models.CharField(max_length=4)
#     blocked = models.CharField(max_length=4)

import pandas as pd
from seas.models import Course_T, Section_T, Classroom_T, Faculty_T

data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
data = data[['CourseID', 'Sec', 'ROOM_ID', 'size', 'stuNo', 'Semester', 'Year', 
            'FACULTY_ID', 'STRAT_TIME', 'END_TIME', 'ST_MW', 'BLOCKED']]
data = data.drop_duplicates()

for index, row in data.iterrows():
    Section_T(course = Course_T.objects.get(courseID = row['CourseID']),
             sectionNo = row('Sec'),
             room = Classroom_T.objects.get(roomID = row['ROOM_ID']),
             capacity = row['size'],
             noOfEnrolledStudent = row['stuNo'],
             semester = row['Semester'],
             year = row['Year'],
             facultyID = Faculty_T.objects.get(facultyID = row['FACULTY_ID']),
             startTime = row['STRAT_TIME'],
             endTime = row['END_TIME'],
             day = row['ST_MW'],
             blocked = row['BLOCKED']).save()
