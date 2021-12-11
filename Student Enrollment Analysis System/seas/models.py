from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE

# These are our SEAS database models built upon our Schema and referenced from our DATA_DICTIONARY.


class School_T(models.Model):
    schoolTitle = models.CharField(max_length=6, primary_key=True)
    schoolName = models.CharField(max_length=50)

    def __str__(self):
        return self.schoolTitle


class Department_T(models.Model):
    deptCode = models.CharField(max_length=3, primary_key=True)
    deptName = models.CharField(max_length=50)
    school = models.ForeignKey(School_T, on_delete=models.CASCADE)

    def __str__(self):
        return self.deptCode


class Faculty_T(models.Model):
    facultyID = models.CharField(primary_key=True, max_length= 10)
    facultyName = models.CharField(max_length=50)

    def __str__(self):
        return self.facultyName


class Course_T(models.Model):
    courseID = models.CharField(max_length=7, primary_key=True)
    courseName = models.CharField(max_length=50)
    creditHour = models.IntegerField()
    dept = models.ForeignKey(Department_T, on_delete=CASCADE)
    
    def __str__(self):
        return self.courseName


class Classroom_T(models.Model):
    roomID = models.CharField(max_length=7, primary_key=True)
    roomCapacity = models.IntegerField()

    def __str__(self):
        return self.roomID


class Section_T(models.Model):
    course = models.ForeignKey(Course_T, on_delete=CASCADE)
    sectionNo = models.IntegerField()
    room = models.ForeignKey(Classroom_T, on_delete=CASCADE)
    capacity = models.IntegerField()
    noOfEnrolledStudent = models.IntegerField()
    semester = models.CharField(max_length=6, default= "N/A")
    year = models.CharField(max_length=4)
    faculty = models.ForeignKey(Faculty_T, on_delete=CASCADE, null=True)
    # startTime = models.TimeField(default= datetime.time(datetime.now()))
    # endTime = models.TimeField(default= datetime.time(datetime.now()))
    day = models.CharField(max_length=4)
    blocked = models.CharField(max_length=4)
    
    def __str__(self):
        return f'{self.course} - Section {self.sectionNo} ({self.semester} {self.year})'