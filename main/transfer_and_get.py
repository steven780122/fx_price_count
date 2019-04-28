import pandas as pd

# FILE_INPUT = 'sample/TEST.xlsx'
FILE_INPUT = 'sample/EURUSD5.csv'

FILE_OUTPUT = 'csvfile.csv'

# data_xls = pd.read_excel('sample/20190424_M5_EURUSD5.xlsx', 'EURUSD5', index_col=None)

# data_xls = pd.read_excel(FILE_INPUT, 'EURUSD5', index_col=None)


# data_xls.to_csv(FILE_OUTPUT, encoding='utf_8_sig', index=False)

data_csv_df = pd.read_csv(FILE_INPUT, header=None)    # cause first row is value not head name
print(data_csv_df)
print('****1***')
open_series = data_csv_df.iloc[:, 2]
high_series = data_csv_df.iloc[:, 3]
print(open_series)
print(type(open_series))
print('****2***')
print(pd.concat([open_series, high_series], ignore_index=True))