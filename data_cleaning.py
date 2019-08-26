import pandas as pd

df = pd.read_csv('../data/all.csv')
df['Date'] = df['DATE'].map(lambda x: x.split('T')[0]).apply(pd.to_datetime) + df['DATE'].map(
    lambda x: x.split('T')[1]).apply(pd.to_timedelta)
# df['Time'] = df['DATE'].map(lambda x: x.split('T')[1]).apply(pd.to_timedelta) + df['Date']
# df['Date'] = df['Date'].map(lambda x: x.split('T')[0]).apply(pd.to_datetime)
df['Temperature'] = df['TMP'].map(lambda x: int(x.split(',')[0]) / 10).apply(pd.to_numeric)
df['Dewpoint'] = df['DEW'].map(lambda x: int(x.split(',')[0]) / 10).apply(pd.to_numeric)
# df = df[['Date', 'Time', 'Temperature', 'Dewpoint']].set_index('Date')


df = df[['Date', 'Temperature', 'Dewpoint']].set_index('Date')

features = ['Date', 'Temperature', 'Dewpoint']

# rows = tmp.shape[0]
#
# nth_prior_measurements = [None] * N + [tmp[feature][i - N] for i in range(N, rows)]
#
# col_name = '{}_{}'.format(feature, N)
# tmp[col_name] = nth_prior_measurements

# 删除不符合常理的数据
for i, row in df.iterrows():
    if any([
        df.loc[i, 'Temperature'] > 50,
        df.loc[i, 'Dewpoint'] > 50
    ]):
        print('Delete %s row' % i)
        df.drop([i], inplace=True)


def derive_nth_day_feature(df, feature, N):
    rows = df.shape[0]
    nth_prior_measurements = [None] * N + [df[feature][index - N] for index in range(N, rows)]
    col_name = '{}_{}'.format(feature, N)
    df[col_name] = nth_prior_measurements


# 提取前三天的数据，并将它们与本日的数据合并为一行
for feature in features:
    if feature != 'Date':
        for N in range(1, 4):
            derive_nth_day_feature(df, feature, N)

spread = df.describe().T  # describe矩阵转置
IQR = spread['75%'] - spread['25%']  # 计算 interquartile range 四分位距 Q3-Q1
# 去掉极端数据
spread['outliers'] = (spread['min'] < (spread['25%'] - (3 * IQR))) | (spread['max'] > (spread['75%'] + 3 * IQR))
# 显示结果
print(spread)
# 删除有空白数据的行

df = df.dropna()

print(df.head())
print(df.info())
print(df.describe())

df.to_csv('../data/all_cleaned.csv')
