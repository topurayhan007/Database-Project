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
    df2 = df.FACULTY_FULL_NAME.str.split("-", expand=True)
    df['FACULTY_ID'] = df2[0]
    df['FACULTY_NAME'] = df2[1]
    df.to_excel(updatefilepath, index = None, header=True)
    print(df)

#convertExcelToCSV("scripts/classSize.xlsx", "scripts/classSize.csv")
#convertTallyExcelToCSV("scripts/TallySheetForAutumn2020.xlsx", "scripts/TallySheetForAutumn2020.csv")
splitFacultyTallyData("scripts/TallySheetForAutumn2020.xlsx", "scripts/tallySplit.xlsx")