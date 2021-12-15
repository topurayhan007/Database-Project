from django.test import TestCase
from seas.models import *
# Create your tests here.

print("School= ")
schoolList = School_T.objects.order_by().values_list('schoolTitle').distinct()
print(School_T.objects.order_by().values_list('schoolTitle').distinct())
print("Semester")
semesterList = Section_T.objects.order_by().values_list('semester').distinct()
# print(Section_T.objects.order_by().values_list('semester').distinct())

yearList = Section_T.objects.order_by().values_list('year').distinct()
# newlist = [[]]
# newlist = [Section_T.objects.order_by().values_list('year').distinct(), Section_T.objects.order_by().values_list('semester').distinct()]
print(semesterList)
print(yearList)
print("hello")