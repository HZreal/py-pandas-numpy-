import pandas

# pandas.DataFrame( data, index, columns, dtype, copy)
# 参数说明：
# data：一组数据(ndarray、series, map, lists, dict 等类型)。
# index：索引值，或者可以称为行标签。
# columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
# dtype：数据类型。
# copy：拷贝数据，默认为 False。

# data1 = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
# dataFrame1 = pandas.DataFrame(data=data1, columns=['Site', 'Age'])
# print(dataFrame1)


# data2 = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
# dataFrame2 = pandas.DataFrame(data=data2)
# print(dataFrame2)


# data3 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# dataFrame3 = pandas.DataFrame(data=data3)
# print(dataFrame3)   # 没有对应的部分数据为 NaN。


data4 = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "fashion": [30, 90, 60]
}
# dataFrame4 = pandas.DataFrame(data=data4)
# print(dataFrame4)
# # 使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推
# print(dataFrame4.loc[0])     # 返回结果其实就是一个 Pandas Series 数据。
# # 返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开
# print(dataFrame4.loc[[0, 1]])     # 返回结果其实就是一个 Pandas DataFrame 数据。

dataFrame5 = pandas.DataFrame(data=data4, index=["day1", "day2", "day3"])
# print(dataFrame5.loc['day1'])
# print(dataFrame5.loc[['day1', 'day3']])       # 取某两行
# print(dataFrame5[['calories', 'fashion']])    # 取某两列

print(dataFrame5.index)  # 返回索引的迭代器
for index in dataFrame5.index:
    print(index)

