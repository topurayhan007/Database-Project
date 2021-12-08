from django.db import models
from django.db.models.deletion import CASCADE

# These are our SEAS database models built upon our Schema and referenced from our DATA_DICTIONARY.


class School_T(models.Model):
    schoolTitle = models.CharField(max_length=6, primary_key=True)
    schoolName = models.CharField(max_length=50)


class Department_T(models.Model):
    deptCode = models.CharField(max_length=3, primary_key=True)
    deptName = models.CharField(max_length=50)
    school = models.ForeignKey(School_T, on_delete=models.CASCADE)


class Faculty_T(models.Model):
    facultyID = models.IntegerField(primary_key=True)
    facultyName = models.CharField(max_length=50)


class Course_T(models.Model):
    courseID = models.CharField(max_length=7, primary_key=True)
    courseName = models.CharField(max_length=50)
    creditHour = models.IntegerField()
    dept = models.ForeignKey(Department_T, on_delete=CASCADE)
    semester = models.CharField(max_length=6)
    year = models.CharField(max_length=4)
    
    def __str__(self):
        return self.courseName


class Classroom_T(models.Model):
    roomID = models.CharField(max_length=7, primary_key=True)
    roomCapacity = models.IntegerField()


class Section_T(models.Model):
    course = models.ForeignKey(Course_T, on_delete=CASCADE)
    sectionNo = models.IntegerField(primary_key=True)
    room = models.ForeignKey(Classroom_T, on_delete=CASCADE)
    capacity = models.IntegerField()
    noOfEnrolledStudent = models.IntegerField()
    faculty = models.ForeignKey(Faculty_T, on_delete=CASCADE)
    startTime = models.TimeField()
    endTime = models.TimeField()
    day = models.CharField(max_length=4)
    blocked = models.CharField(max_length=4)
