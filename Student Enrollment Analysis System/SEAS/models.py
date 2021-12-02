from django.db import models

# Create your models here.

class School (models.Model):
    schoolTitle = models.CharField(max_length = 6)
    schoolName = models.CharField(max_length = 50)

class Department (models.Model):
    deptCode = models.CharField(max_length = 3)
    deptName = models.CharField(max_length = 50)
    schoolTitle = models.CharField(max_length = 6)

class Faculty (models.Model):
    facultyID = models.IntegerField()
    facultyName = models.CharField(max_length = 50)
    deptCode = models.CharField(max_length = 3)

class Course (models.Model):
    courseID = models.CharField(max_length = 7)
    courseName = models.CharField(max_length = 50)
    creditHour = models.IntegerField()
    deptcode = models.CharField(max_length = 3)
    semester = models.CharField(max_length = 6)
    year = models.DateField()

class Classroom (models.Model):
    roomID = models.CharField(max_length = 7)
    roomCapacity = models.IntegerField()

class Section (models.Model):
    courseID = models.CharField(max_length = 7)
    sectionNo = models.IntegerField()
    semester = models.CharField(max_length = 6)
    year = models.DateField()
    roomID = models.CharField(max_length = 7)
    capacity = models.IntegerField()
    noOfEnrolledStudent = models.IntegerField()
    facultyID = models.IntegerField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    day = models.CharField(max_length = 4)
    blocked = models.CharField(max_length = 4)


