
import pandas

df = pandas.read_csv('nba.csv')   # DataFrame对象
# print(df)
# to_string() 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替。
# print(df.to_string())


# 使用 to_csv() 方法将 DataFrame 存储为 csv 文件：
# name = ["Google", "Runoob", "Taobao", "Wiki"]
# site = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
# age = [90, 40, 80, 98]
# _dict = {'name': name, 'site': site, 'age': age}
# df2 = pandas.DataFrame(data=_dict)
# # 保存 dataframe 为 CSV 文件
# df2.to_csv('_test.csv')


# head( n ) 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行。
# print(df.head())
# tail( n ) 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN。
# print(df.tail())
# info() 方法返回表格的一些基本信息：
print(df.info())












