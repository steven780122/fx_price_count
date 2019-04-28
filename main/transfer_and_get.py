import pandas as pd

data_xls = pd.read_excel('sample/20190424_M5_EURUSD5.xlsx', 'EURUSD5', index_col=None)
# read_excel('excelfile.xlsx', 'Sheet2', index_col=None)
print(data_xls)

data_xls.to_csv('csvfile.csv', encoding='utf_8_sig', index=False)

