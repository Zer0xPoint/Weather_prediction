import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    '/Users/lee/Library/CloudStorage/iCloudDrive/Documents/PyCharmProjects/Weather_prediction/data/all_clean.csv')
# 计算皮尔逊相关 相关度由-1到1
df.corr()[['Temperature']].sort_values('Temperature')
# 去掉相关性小于0.6的列

df2 = df[
    ['Temperature'] + ['Dewpoint', 'Dewpoint_1', 'Dewpoint_2', 'Dewpoint_3', 'Temperature_1', 'Temperature_2',
                       'Date']].set_index('Date')  # Date与温度关系为非线性，为了预览方便故增加Date列

predictors = ['Dewpoint', 'Dewpoint_1', 'Dewpoint_2', 'Dewpoint_3', 'Temperature_1', 'Temperature_2']
fig, axes = plt.subplots(nrows=3, ncols=2)
arr = np.array(predictors).reshape(3, 2)

for row, col_arr in enumerate(arr):
    for col, feature in enumerate(col_arr):
        axes[row, col].scatter(df2[feature], df2['Temperature'])
        if col == 0:
            axes[row, col].set(xlabel=feature, ylabel='Temperature')
        else:
            axes[row, col].set(xlabel=feature)
plt.show()

df2.to_csv(
    '/Users/lee/Library/CloudStorage/iCloudDrive/Documents/PyCharmProjects/Weather_prediction/data/all_clean.csv')
