import pandas as pd
import numpy as np

# pd.DataFrame( data, index, columns, dtype, copy)
# 参数说明：
# data：一组数据(ndarray、series, map, lists, dict 等类型)。
# index：行索引，或者可以称为行标签。
# columns：列索引，或称为列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
# dtype：数据类型。
# copy：拷贝数据，默认为 False。

# data1 = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
# df1 = pd.DataFrame(data=data1, columns=['Site', 'Age'])   # 指定列索引
# print(df1)

# data2 = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
# df2 = pd.DataFrame(data=data2)
# print(df2)

# data3 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# df3 = pd.DataFrame(data=data3)
# print(df3)   # 没有对应的部分数据为 NaN。


# data4 = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45],
#     "fashion": [30, 90, 60]
# }
# df4 = pd.DataFrame(data=data4)
# print(df4)
# # 使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推
# print(df4.loc[0])     # 返回结果其实就是一个 pandas Series 数据。
# # 返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开
# print(df4.loc[[0, 1]])     # 返回结果其实就是一个 pd DataFrame 数据。

# df5 = pd.DataFrame(data=data4, index=["day1", "day2", "day3"])
# print(df5.loc['day1'])
# print(df5.loc[['day1', 'day3']])       # 取某两行
# print(df5[['calories', 'fashion']])    # 取某两列

# print(df5.index)  # 返回索引的迭代器
# for index in df5.index:
#     print(index)



stock_change = np.random.normal(0, 1, (10, 5))
print('stock_change------\n', stock_change)
row_index = ['行索引{}'.format(i+1) for i in range(stock_change.shape[0])]
print('行索引----------\n', row_index)
col_index = pd.date_range(start='2021-9-1', periods=stock_change.shape[1], freq='B')
print('列索引----------\n', col_index)
df = pd.DataFrame(stock_change, index=row_index, columns=col_index)
print('dataFrame--------\n', df)

# DataFrame的属性
shape, index, col, values, T, head, tail = df.shape, df.index, df.columns, df.values, df.T, df.head(), df.tail(3)

# 设置行/列索引必须整体设置，不能单个设置
df.index = ['修改----行索引{}'.format(i+1) for i in range(stock_change.shape[0])]
print('修改行索引-------\n', df)
print('获取第四行索引------\n', df.index[3])
# df.index[3] = 'hhhhhhhh'    # 报错，不能单个设置

# 重设索引函数
df.reset_index(drop=True)   # drop表示是否在原数据上删除索引
print('重-------\n', df)

# 以某列设置多个索引
df.set_index(['2021-9-1', '2021-9-1'], drop=True)
print('设置列索引--------\n', df)




