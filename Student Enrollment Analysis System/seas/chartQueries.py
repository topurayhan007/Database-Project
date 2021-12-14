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
            AND semester = "Summer" AND YEAR = '2021'
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
            AND semester = "Summer" AND YEAR = '2021'
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
            AND semester = "Summer" AND YEAR = '2021'
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
            AND semester = "Summer" AND YEAR = '2021'
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
            AND semester = "Summer" AND YEAR = '2021'
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
            AND semester = "Summer" AND YEAR = '2021'
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
            AND semester = "Summer" AND YEAR = '2021'
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
            AND semester = "Summer" AND YEAR = '2021'
        '''.format(semester,year,semester,year,semester,year,semester,year,semester,year,semester,year,semester,year,semester,year))
        result = cursor.fetchall()
    return result