#ClassSizeDistribution Chart query

school_id = 'SBE'

query = '''
    --------ClassSizeDistribution------------
    SELECT COUNT(*) AS School_SBE
    FROM (SELECT *
        FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
        INNER JOIN seas_section_t ON course_id=courseid)
    WHERE noofenrolledstudent BETWEEN 1 AND 10
    AND semester = "Summer" AND YEAR = '2021' AND school_id = "{}"
    ------------------------------------------------------------------------------------
    UNION ALL
    ------------------------------------------------------------------------------------
    SELECT COUNT(*)
    FROM (SELECT *
        FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
        INNER JOIN seas_section_t ON course_id=courseid)
    WHERE noofenrolledstudent BETWEEN 11 AND 20
    AND semester = "Summer" AND YEAR = '2021' AND school_id = "{}"
    ------------------------------------------------------------------------------------
    UNION ALL
    ------------------------------------------------------------------------------------
    SELECT COUNT(*)
    FROM (SELECT *
        FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
        INNER JOIN seas_section_t ON course_id=courseid)
    WHERE noofenrolledstudent BETWEEN 21 AND 30
    AND semester = "Summer" AND YEAR = '2021' AND school_id = "{}"
    ------------------------------------------------------------------------------------
    UNION ALL
    ------------------------------------------------------------------------------------
    SELECT COUNT(*)
    FROM (SELECT *
        FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
        INNER JOIN seas_section_t ON course_id=courseid)
    WHERE noofenrolledstudent BETWEEN 31 AND 35
    AND semester = "Summer" AND YEAR = '2021' AND school_id = "{}"
    ------------------------------------------------------------------------------------
    UNION ALL
    ------------------------------------------------------------------------------------
    SELECT COUNT(*)
    FROM (SELECT *
        FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
        INNER JOIN seas_section_t ON course_id=courseid)
    WHERE noofenrolledstudent BETWEEN 36 AND 40
    AND semester = "Summer" AND YEAR = '2021' AND school_id = "{}"
    ------------------------------------------------------------------------------------
    UNION ALL
    ------------------------------------------------------------------------------------
    SELECT COUNT(*)
    FROM (SELECT *
        FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
        INNER JOIN seas_section_t ON course_id=courseid)
    WHERE noofenrolledstudent BETWEEN 41 AND 50
    AND semester = "Summer" AND YEAR = '2021' AND school_id = "{}"
    ------------------------------------------------------------------------------------
    UNION ALL
    ------------------------------------------------------------------------------------
    SELECT COUNT(*)
    FROM (SELECT *
        FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
        INNER JOIN seas_section_t ON course_id=courseid)
    WHERE noofenrolledstudent BETWEEN 51 AND 55
    AND semester = "Summer" AND YEAR = '2021' AND school_id = "{}"
    ------------------------------------------------------------------------------------
    UNION ALL
    ------------------------------------------------------------------------------------
    SELECT COUNT(*)
    FROM (SELECT *
        FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
        INNER JOIN seas_section_t ON course_id=courseid)
    WHERE noofenrolledstudent BETWEEN 56 AND 60
    AND semester = "Summer" AND YEAR = '2021' AND school_id = "{}"
    ------------------------------------------------------------------------------------
    UNION ALL
    ------------------------------------------------------------------------------------
    SELECT COUNT(*)
    FROM (SELECT *
        FROM seas_department_t INNER JOIN seas_course_t ON deptcode=dept_id
        INNER JOIN seas_section_t ON course_id=courseid)
    WHERE noofenrolledstudent > 60
    AND semester = "Summer" AND YEAR = '2021' AND school_id = "{}"

'''.format(school_id, school_id, school_id, school_id, school_id, school_id, school_id, school_id, school_id)

print(query)