import pandas as pd

folder_path = r'/Users/lee/Library/CloudStorage/iCloudDrive/Documents/PyCharmProjects/Weather_prediction/2017' \
              r'-2019_ZhaoTong_Dataset'
save_path = r'/Users/lee/Library/CloudStorage/iCloudDrive/Documents/PyCharmProjects/Weather_prediction/data/all.csv'

file_list = ['1.csv', '2.csv', '3.csv']  # listdir读取出来文件是乱序，手动确认顺序

df = pd.read_csv(folder_path + '/' + file_list[0], usecols=['DATE', 'TMP'])  # 指定cols选择文件中的两列作为DataFrame，忽略其余无关列，节省时间和空间
df.to_csv(save_path, encoding="utf_8_sig", index=False)

for i in range(1, len(file_list)):
    df = pd.read_csv(folder_path + '/' + file_list[i], usecols=['DATE', 'TMP'])
    df.to_csv(save_path, encoding="utf_8_sig", index=False, header=False, mode='a+')  # 保存在上一个文件最后一行之后，忽略headers表头
