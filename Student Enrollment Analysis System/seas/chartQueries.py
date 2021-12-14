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

# arr1 = ClassSizeRequirement("Spring", '2021')
# arr2 = ClassSizeRequirement("Summer", '2021')
# arr3 = np.concatenate((arr1, arr2), axis=1)
# sumarr = arr3.sum(axis=0)
# res = np.array([])
# #resu = np.row_stack((arr3, sumarr), axis= 0)
# resu = np.concatenate((arr3, sumarr), axis= 0)
# print(arr3)
# print(sumarr)
# print(resu)


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
# sels = ClassSizeDistribution("Spring", '2021', "SELS")
# sets = ClassSizeDistribution("Spring", '2021', "SETS")
# slass = ClassSizeDistribution("Spring", '2021', "SLASS")
# spph = ClassSizeDistribution("Spring", '2021', "SPPH")
# allarr = np.concatenate((sbe, sels, sets, slass, spph), axis=1)
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