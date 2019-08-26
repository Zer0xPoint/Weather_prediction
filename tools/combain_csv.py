import pandas as pd
import os

folder_path = r'/Users/lee/Library/CloudStorage/iCloudDrive/Documents/PyCharmProjects/Weather_prediction/2017-2019_ZhaoTong_Dataset'
save_path = r'/Users/lee/Library/CloudStorage/iCloudDrive/Documents/PyCharmProjects/Weather_prediction/2017-2019_ZhaoTong_Dataset'
save_name = r'all.csv'

os.chdir(folder_path)
file_list = os.listdir()  # 将程序地址改为需要合并文件所在的文件夹

df = pd.read_csv(folder_path + '/' + file_list[0])

df.to_csv(save_path + '/' + save_name, encoding="utf_8_sig", index=False)  # 读取第一个文件的表头并保存

for i in range(1, len(file_list)):  # 在读取之后的文件时，无需读取表头
    df = pd.read_csv(folder_path + '/' + file_list[i])
    df.to_csv(save_path + '/' + save_name, encoding="utf_8_sig", index=False, header=False, mode='a+')  # 保存在上一个文件最后一行之后
