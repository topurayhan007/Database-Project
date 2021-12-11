import pandas as pd
from seas.models import Faculty_T

data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
data = data.FACULTY_FULL_NAME.str.split('-')

data = data.drop_duplicates()

for item in data:
    try:
        Faculty_T(facultyID=item[0], facultyName=item[1]).save()
    except ValueError:
        continue