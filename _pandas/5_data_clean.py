import pandas

# Pandas 清洗空值
# 删除包含空字段的行，可以使用 dropna() 方法，语法格式如下：
# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
# how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
# thresh：设置需要多少非空值的数据才可以保留下来的。
# subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
# inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。
# 通过 isnull() 判断各个单元格是否为空。

df1 = pandas.read_csv('property-data.csv')
# print(df1['NUM_BEDROOMS'])
# print(df1['NUM_BEDROOMS'].isnull())
# 通过上述输出，Pandas 把 n/a 和 NA 当作空数据，na 不是空数据，不符合我们要求，我们可以指定空数据类型：
# missing_values = ["n/a", "na", "--"]
# df2 = pandas.read_csv('property-data.csv', na_values = missing_values)
# print(df2)
# print(df2['NUM_BEDROOMS'])
# print(df2['NUM_BEDROOMS'].isnull())
# 删除包含空数据的行
# new_df = df1.dropna()  # 默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据
# print(new_df.to_string())
# 如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数:
# df1.dropna(inplace=True)
# print(df1.to_string())
# 移除指定列有空值的行
# df1.dropna(subset=['ST_NUM'], inplace=True)
# print(df1.to_string())
# fillna() 方法 使用指定数据来替换空数据
# df1.fillna(123456, inplace=True)
# print(df1.to_string())
# 指定某一个列来替换数据：
# df1['PID'].fillna(123456, inplace=True)
# print(df1)

# 替换空单元格的常用方法是计算列的均值、中位数值或众数。
# Pandas使用 mean()、median() 和 mode() 方法计算列的均值（所有值加起来的平均值）、中位数值（排序后排在中间的数）和众数（出现频率最高的数）
# col_avg = df1['ST_NUM'].mean()
# print(col_avg)
# col_median = df1['ST_NUM'].median()
# print(col_median)
# col_mode = df1['ST_NUM'].mode()
# print(col_mode)


# Pandas 清洗格式错误数据
# 通过包含空单元格的行，或者将列中的所有单元格转换为相同格式的数据
# 第三个日期格式错误
# data = {
#   "Date": ['2020/12/01', '2020/12/02' , '20201226'],
#   "duration": [50, 40, 45]
# }
# df3 = pandas.DataFrame(data, index=['day1', 'day2', 'day3'])
# print(df3)
# df3['Date'] = pandas.to_datetime(df3['Date'], format='%Y-%m-%d')
# print(df3)


# Pandas 清洗错误数据
# 对错误的数据进行替换或移除
person = {
    "name": ['Google', 'Runoob', 'Taobao', 'Runoob'],
    "age": [50, 200, 12345, 200]  # 12345 年龄数据是错误的
}
df4 = pandas.DataFrame(person)
# print(df4)
# 修改数据
# df4.loc[2, 'age'] = 30
# print(df4.to_string())
# 设置条件语句
# for x in df4.index:
#     if df4.loc[x, 'age'] > 120:
#         df4.loc[x, 'age'] = 120
#     else:
#         df4.drop(x, inplace=True)   # 删除索引行
# print(df4.to_string())



# Pandas 清洗重复数据
# 清洗重复数据，可以使用 duplicated() 和 drop_duplicates() 方法
print(df4.duplicated())  # 对应的数据行是重复的，duplicated() 会返回 True
df4.drop_duplicates(inplace=True)
print(df4)








