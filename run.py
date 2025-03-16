import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import Trainning
'''
预期输入为csv格式

第1列为协议号

第2列开始为输出信号
lengthOfOutput是输出信号的数量 代码会对所有输出信号进行计算

Example： lengthOfOutput = 5
从第2列到第7列为输出信号，总共5个
第七列以后的是抓取到的数据帧，以bit形式一列一个出现

'''
# 是否输出所有信息？
verbose = 0
lengthOfOutput = 1

# 读取 CSV 文件
df = pd.read_csv("target.csv")
print(type(df))
# 将 DataFrame 转换为 NumPy 数组
data = df.to_numpy()  # 或者用 df.values



protocalDict = {}          # 用于存放 协议号 -> [行1, 行2, ...] 的映射

for i in range(data.shape[0]):
    protocol_id = data[i, 0]      # 第 i 行的协议号（假设 data[i, 0] 是数值）
    current_row = data[i, :]      # 第 i 行的所有数据

    # 如果协议号不存在，则创建一个空列表
    if protocol_id not in protocalDict:
        protocalDict[protocol_id] = []

    # 将当前行数据追加到对应协议号下
    protocalDict[protocol_id].append(current_row)



for key in protocalDict:

    trainingData = protocalDict[key]

    arr = np.array(trainingData) #转换为np对象

    for index in range(0,lengthOfOutput):
        print("Data from protocal", end=" ")
        print(key)
        print("To output Variable", end=" ")
        print(index)

        targetVariable = arr[:, [1+index]]  # 结果是 (n, 1) 矩阵,取出index 1的一整列

        dataIndex = 1+lengthOfOutput
        characteristicVariable = arr[:, dataIndex:]  # 从index 2 到最后一列 (include index 2)

        Trainning.Train(targetVariable,characteristicVariable,verbose)



