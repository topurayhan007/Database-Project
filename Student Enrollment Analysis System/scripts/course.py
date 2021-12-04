import pandas as pd
data_xls = pd.read_excel('scripts/classSize.xlsx', 'Data', dtype=str, index_col=None)
data_xls.to_csv('scripts/classSize.xlsx', encoding='utf-8', index=False)