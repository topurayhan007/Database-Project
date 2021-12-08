import pandas as pd
from seas.models import School_T, Department_T, Faculty_T, Course_T, Classroom_T, Section_T

def populateDatabase(filepath):
    df = pd.read_excel(filepath, header=3, skipfooter=1, engine= 'openpyxl')
    df.to_csv ("scripts/TallySheetForAutumn2020.csv", index = None, header=True)
    df = pd.read_csv ("scripts/TallySheetForAutumn2020.csv")
    print(df)

filepath = "scripts/TallySheetForAutumn2020.xlsx"
populateDatabase(filepath)