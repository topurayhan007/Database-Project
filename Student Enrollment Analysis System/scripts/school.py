import pandas as pd
from seas.models import School_T

data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
data = set(data.SCHOOL_TITLE)

for item in data:
    School_T(schoolTitle=item).save()
