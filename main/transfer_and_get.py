import pandas as pd

# FILE_INPUT = 'sample/TEST.xlsx'
# FILE_INPUT = 'sample/EURUSD5.csv'
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
low_series = data_csv_df.iloc[:, 4]
close_series = data_csv_df.iloc[:, 5]
print(open_series)
print(type(open_series))
print('****2***')
concat_series = pd.concat([open_series, high_series, low_series, close_series], ignore_index=True)
print(concat_series)

print('****3***')
price_counts = concat_series.value_counts()
print(price_counts)
head_sortbyprice = price_counts.head(200).sort_index(ascending=False)
print(head_sortbyprice)    # sort by index (want to list price from low to high)
head_sortbyprice.to_frame().to_csv(FILE_OUTPUT)      # get top high counts's price

