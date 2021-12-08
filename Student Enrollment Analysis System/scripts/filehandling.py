import pandas as pd
import os

def convertExcelToCSV(filepath, updatefilepath):
    read_file = pd.read_excel(filepath, engine = 'openpyxl')

    read_file.to_csv (updatefilepath, index = None, header=True)

    df = pd.read_csv(updatefilepath)

    print(df)


def convertTallyExcelToCSV(filepath, updatefilepath):
    read_file = pd.read_excel(filepath, header=3, skipfooter=1, engine = 'openpyxl')

    read_file.to_csv (updatefilepath, index = None, header=True)

    df = pd.read_csv(updatefilepath)

    print(df)


def splitFacultyTallyData(filepath, updatefilepath):

    df = pd.read_excel(filepath,  header=3, skipfooter=1, engine= 'openpyxl')
    column_name = 'FACULTY_FULL_NAME'
    value1 = []
    value2 = []
    value3 = []
    value4 = []
    value5 = []
    value6 = []
    value7 = []
    value8 = []
    value9 = []
    value10 = []
    value11 = []
    value12 = []
    value13 = []
    value14 = []
    value15 = []

    for i in range(df['FACULTY_FULL_NAME'].size):
        value1 = df['SCHOOL_TITLE']
        value2 = df['COFFER_COURSE_ID']
        value3 = df['COFFERED_WITH']
        value4 = df['SECTION']
        value5 = df['CREDIT_HOUR']
        value6 = df['CAPACITY']
        value7 = df['ENROLLED']
        value8 = df['ROOM_ID']
        value9 = df['ROOM_CAPACITY']
        value10 = df['BLOCKED']
        value11 = df['COURSE_NAME']
        value12 = df['FACULTY_FULL_NAME']
        value13 = df['STRAT_TIME']
        value14 = df['END_TIME']
        value15 = df['ST_MW']

    #df = pd.DataFrame({ 'FACULTY_FULL_NAME': value })
    df = pd.DataFrame({'SCHOOL_TITLE':value1,'COFFER_COURSE_ID':value2,'COFFERED_WITH':value3,'SECTION':value4,
                    'CREDIT_HOUR':value5,'CAPACITY':value6,'ENROLLED':value7,'ROOM_ID':value8,'ROOM_CAPACITY':value9,
                    'BLOCKED':value10,'COURSE_NAME':value11,'FACULTY_FULL_NAME':value12,'STRAT_TIME':value13,
                    'END_TIME':value14,'ST_MW':value15})
    
    df2 = df.FACULTY_FULL_NAME.str.split("-", expand=True)
    df['FACULTY_ID'] = df2[0]
    df['FACULTY_NAME'] = df2[1]
    df.to_excel(updatefilepath, index = None, header=True)

    print(df)

#convertExcelToCSV("scripts/classSize.xlsx", "scripts/classSize.csv")
#convertTallyExcelToCSV("scripts/TallySheetForAutumn2020.xlsx", "scripts/TallySheetForAutumn2020.csv")
splitFacultyTallyData("scripts/TallySheetForAutumn2020.xlsx", "scripts/tallySplit.xlsx")