import pandas as pd
from seas.models import School_T

data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
data = set(data.SCHOOL_TITLE)

for item in data:
    if item == "SPPH":
        School_T(schoolTitle=item, schoolName = "School of Pharmacy and Public Health").save()
    elif item == "SLASS":
        School_T(schoolTitle=item, schoolName = "School of Liberal Arts & Social Sciences").save()
    elif item == "SETS":
        School_T(schoolTitle=item, schoolName = "School of Engineering, Technology & Sciences").save()
    elif item == "SELS":
        School_T(schoolTitle=item, schoolName = "School of Environment and Life Sciences").save()
    elif item == "SBE":
        School_T(schoolTitle=item, schoolName = "School of Business and Entrepreneurship").save()