import pandas as pd
from seas.models import Classroom_T

data = pd.read_excel('scripts/Revenue.xlsx', sheet_name='Data')
data = data[['ROOM_ID', 'RoomSize']]

data = data.drop_duplicates()
for i in range(data.shape[0]):
    Classroom_T(roomID=data.iloc[i, 0], roomCapacity=data.iloc[i, 1]).save()