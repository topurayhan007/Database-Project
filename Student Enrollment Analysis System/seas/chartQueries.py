from django.db import connection
import numpy as np

def ClassSizeRequirement(semester, year):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(*),
            ROUND((COUNT(*)/12.0),2),
            ROUND((COUNT(*)/14.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 1 AND 10
            AND semester = "{}" AND YEAR = '{}'
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*),
            ROUND((COUNT(*)/12.0),2),
            ROUND((COUNT(*)/14.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 11 AND 20
            AND semester = "{}" AND YEAR = '{}'
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*),
            ROUND((COUNT(*)/12.0),2),
            ROUND((COUNT(*)/14.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 21 AND 30
            AND semester = "{}" AND YEAR = '{}'
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*),
            ROUND((COUNT(*)/12.0),2),
            ROUND((COUNT(*)/14.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 31 AND 35
            AND semester = "{}" AND YEAR = '{}'
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*),
            ROUND((COUNT(*)/12.0),2),
            ROUND((COUNT(*)/14.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 36 AND 40
            AND semester = "{}" AND YEAR = '{}'
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*),
            ROUND((COUNT(*)/12.0),2),
            ROUND((COUNT(*)/14.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 41 AND 50
            AND semester = "{}" AND YEAR = '{}'
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*),
            ROUND((COUNT(*)/12.0),2),
            ROUND((COUNT(*)/14.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 51 AND 55
            AND semester = "{}" AND YEAR = '{}'
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*),
            ROUND((COUNT(*)/12.0),2),
            ROUND((COUNT(*)/14.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 56 AND 65
            AND semester = "{}" AND YEAR = '{}'
        '''.format(semester,year,semester,year,semester,year,semester,year,semester,year,semester,year,semester,year,semester,year))
        result = cursor.fetchall()
    return result

# finalarr = ClassSizeRequirement("Spring", '2021')
# finalarr = np.array(finalarr)
# totalarr = finalarr.sum(axis=0)
# totalarr = np.reshape(totalarr, [1, 3])
# After reshape getting this
# [[1.250e+02 1.042e+01 8.930e+00]
#  [1.700e+02 1.417e+01 1.214e+01]
#  [1.610e+02 1.342e+01 1.150e+01]
#  [1.000e+02 8.330e+00 7.140e+00]
#  [1.150e+02 9.580e+00 8.210e+00]
#  [2.050e+02 1.708e+01 1.464e+01]
#  [4.600e+01 3.830e+00 3.290e+00]
#  [7.000e+00 5.800e-01 5.000e-01]
#  [9.290e+02 7.741e+01 6.635e+01]]
# table = np.concatenate((finalarr, totalarr), axis=0)
# print(finalarr)
# totalarr = finalarr.sum(axis=0)
# print(totalarr)
# print(table)


def ClassSizeDistribution(semester, year, school):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(*)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 1 AND 10
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 11 AND 20
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 21 AND 30
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 31 AND 35
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 36 AND 40
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 41 AND 50
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 51 AND 55
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 56 AND 60
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT COUNT(*)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent > 60
            AND semester = "{}" AND YEAR = '{}' AND school_id = "{}"
        '''.format(semester,year,school, semester,year,school, semester,year,school, semester,year,school, semester,year,school, semester,year,school, semester,year,school, semester,year,school, semester,year,school))
        result = cursor.fetchall()
    return result


# print(ClassSizeDistribution("Spring", '2021', "SETS"))
# sbe = ClassSizeDistribution("Spring", '2021', "SBE") 
# print(sbe)
# sels = ClassSizeDistribution("Spring", '2021', "SELS")
# sets = ClassSizeDistribution("Spring", '2021', "SETS")
# slass = ClassSizeDistribution("Spring", '2021', "SLASS")
# spph = ClassSizeDistribution("Spring", '2021', "SPPH")
# allarr = np.concatenate((sbe, sels, sets, slass, spph), axis=1)
# # # for i in allarr:
# # #     print(i)
# print(allarr)
# totalarr = allarr.sum(axis=1)
# print(totalarr)
# finalarr = np.concatenate((allarr,totalarr),axis=1)
# print(finalarr)



def UsageOfTheResources(semester, year):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT 
            ROUND(sum(capacity),2),
            ROUND(avg(noofenrolledstudent),2),
            ROUND(avg(capacity),2),
            ROUND((avg(capacity)-avg(noofenrolledstudent)),2),
            ROUND(((avg(capacity)-avg(noofenrolledstudent))/avg(capacity)*100),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE semester = "{}" AND YEAR = '{}'
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT
            ROUND(sum(capacity),2),
            ROUND(avg(noofenrolledstudent),2),
            ROUND(avg(capacity),2),
            ROUND((avg(capacity)-avg(noofenrolledstudent)),2),
            ROUND(((avg(capacity)-avg(noofenrolledstudent))/avg(capacity)*100),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE semester = "{}" AND YEAR = '{}' AND school_id = "SBE"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT
            ROUND(sum(capacity),2),
            ROUND(avg(noofenrolledstudent),2),
            ROUND(avg(capacity),2),
            ROUND((avg(capacity)-avg(noofenrolledstudent)),2),
            ROUND(((avg(capacity)-avg(noofenrolledstudent))/avg(capacity)*100),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE semester = "{}" AND YEAR = '{}' AND school_id = "SELS"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT
            ROUND(sum(capacity),2),
            ROUND(avg(noofenrolledstudent),2),
            ROUND(avg(capacity),2),
            ROUND((avg(capacity)-avg(noofenrolledstudent)),2),
            ROUND(((avg(capacity)-avg(noofenrolledstudent))/avg(capacity)*100),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE semester = "{}" AND YEAR = '{}' AND school_id = "SETS"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT
            ROUND(sum(capacity),2),
            ROUND(avg(noofenrolledstudent),2),
            ROUND(avg(capacity),2),
            ROUND((avg(capacity)-avg(noofenrolledstudent)),2),
            ROUND(((avg(capacity)-avg(noofenrolledstudent))/avg(capacity)*100),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE semester = "{}" AND YEAR = '{}' AND school_id = "SLASS"
            ------------------------------------------------------------------------------------
            UNION ALL
            ------------------------------------------------------------------------------------
            SELECT
            ROUND(sum(capacity),2),
            ROUND(avg(noofenrolledstudent),2),
            ROUND(avg(capacity),2),
            ROUND((avg(capacity)-avg(noofenrolledstudent)),2),
            ROUND(((avg(capacity)-avg(noofenrolledstudent))/avg(capacity)*100),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE semester = "{}" AND YEAR = '{}' AND school_id = "SPPH"
        '''.format(semester,year,semester,year,semester,year,semester,year,semester,year,semester,year))
        result = cursor.fetchall()
    return result

# arr = UsageOfTheResources("Spring", '2021')
# Getting 3.5212e+04 instead of 35212.0 when doing np.array(arr)
# arr = np.array(arr)
# print(arr)
# table = UsageOfTheResources("Summer", '2020')
# # for i in table:
# #     print(i)
# print(table)



def EnrollmentBreakdownOfSchool(stuNo, school, year, semester):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT count (*)
            FROM seas_section_t AS s INNER JOIN seas_course_t AS c ON s.course_id = c.courseID 
            INNER JOIN seas_department_t AS d ON c.dept_id = d.deptCode
            WHERE s.noofenrolledstudent= {} AND d.school_id = "{}" AND year= '{}' AND s.semester= "{}"
        '''.format(stuNo, school,  year, semester))
        result = cursor.fetchall()
    return result

# test = EnrollmentBreakdownOfSchool(5, "SBE", '2021', "Spring")
# test = str(test)[2:-3]
# test = int(test) + 1          
# print(test)



def IUBavailableResources():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(*), (COUNT(*)*20)
            FROM seas_classroom_t
            WHERE roomcapacity = 20
            ------------------------------
            UNION ALL
            ------------------------------
            SELECT COUNT(*), (COUNT(*)*30)
            FROM seas_classroom_t
            WHERE roomcapacity = 30
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*35)
            FROM seas_classroom_t
            WHERE roomcapacity = 35
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*40)
            FROM seas_classroom_t
            WHERE roomcapacity = 40
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*50)
            FROM seas_classroom_t
            WHERE roomcapacity = 50
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*54)
            FROM seas_classroom_t
            WHERE roomcapacity = 54
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*64)
            FROM seas_classroom_t
            WHERE roomcapacity = 64
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*124)
            FROM seas_classroom_t
            WHERE roomcapacity = 124
            -----------------------------
            UNION ALL
            -----------------------------
            SELECT COUNT(*), (COUNT(*)*168)
            FROM seas_classroom_t
            WHERE roomcapacity = 168
        ''')
        result = cursor.fetchall()
    return result

# test = IUBavailableResources()
# test = np.array(test)
# print(test)


def AvailabilityAndCourseOfferingComparison(semester, year):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 1 AND 20
            AND semester = "{}" AND YEAR = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 21 AND 30
            AND semester = "{}" AND YEAR = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 31 AND 35
            AND semester = "{}" AND YEAR = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 36 AND 40
            AND semester = "{}" AND YEAR = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 41 AND 50
            AND semester = "{}" AND YEAR = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 51 AND 54
            AND semester = "{}" AND YEAR = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 55 AND 64
            AND semester = "{}" AND YEAR = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 65 AND 124
            AND semester = "{}" AND YEAR = '{}'
            -----------------------------------------------------------------------
            UNION ALL
            -----------------------------------------------------------------------
            SELECT ROUND((COUNT(*)/12.0),2)
            FROM (SELECT *
                FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
                INNER JOIN seas_section_t ON course_id=courseid)
            WHERE noofenrolledstudent BETWEEN 125 AND 168
            AND semester = "{}" AND YEAR = '{}'
        '''.format(semester, year,semester, year,semester, year,semester, year,semester, year,semester, year,semester, year,semester, year,semester, year,semester, year))
        result = cursor.fetchall()
    return result

# test = AvailabilityAndCourseOfferingComparison("Spring", '2021')
# test = np.array(test)
# print(test)


def RevenueTrendOfTheSchools(school, semester, year):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT  SUM(s.noofenrolledstudent * c.credithour)
            FROM seas_section_t AS s INNER JOIN seas_course_t AS c ON s.course_id = c.courseID 
            INNER JOIN seas_department_t AS d on c.dept_id = d.deptCode
            WHERE d.school_id= "{}" AND s.semester= "{}" AND s.year = '{}'
        '''.format(school, semester, year))
        result = cursor.fetchall()
    return result

# test = RevenueTrendOfTheSchools("SBE", "Spring", '2009')
# test = np.array(test).flatten()
# print(test)



def RevenueInEngineeringSchool(dept, semester, year):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT  SUM(s.noofenrolledstudent * c.credithour)
            FROM seas_section_t AS s INNER JOIN seas_course_t AS c ON s.course_id = c.courseID 
            INNER JOIN seas_department_t AS d on c.dept_id = d.deptCode
            WHERE d.deptcode= "{}" AND s.semester= "{}" AND s.year = '{}'
        '''.format(dept, semester, year))
        result = cursor.fetchall()
    return result


# test = RevenueInEngineeringSchool("CSE", "Spring", '2009')
# test = np.array(test).flatten()
# print(test)