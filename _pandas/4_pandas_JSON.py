import json

from glom.core import glom
import pandas
from pandas import DataFrame, Series

# df = pandas.read_json('site.json')
# print(df.to_string())

# JSON 对象与 Python 字典具有相同的格式，所以我们可以直接将 Python 字典转化为 DataFrame 数据
# 字典格式的 JSON
# s = {
#     "col1": {"row1": 1, "row2": 2, "row3": 3},
#     "col2": {"row1": "x", "row2": "y", "row3": "z"}
# }
# # 读取 JSON 转为 DataFrame
# df1 = pandas.DataFrame(s)
# print(df1)


# 从 URL 中读取 JSON 数据
# URL = 'https://static.runoob.com/download/sites.json'
# df2 = pandas.read_json(URL)
# print(df2)


# 内嵌的 JSON 数据文件的解析
# df3 = pandas.read_json('nested_list.json')
# print(df3)
# 就需要使用到 json_normalize() 方法将内嵌的数据完整的解析出来
# with open('nested_list.json','r') as f:
#     data = json.loads(f.read())
# 展平数据
# df_nested_list: DataFrame = pandas.json_normalize(data, record_path =['students'])   # 使用了参数 record_path 并设置为 ['students'] 用于展开内嵌的 JSON 数据 students。
# df_nested_list = pandas.json_normalize(data, record_path =['students'], meta=['school_name', 'class'])   # 显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数来显示这些元数据：
# print(df_nested_list)


# 更复杂的内嵌 JSON 数据
# with open('nested_mix.json', 'r') as f:
#     data = json.loads(f.read())
# df4 = pandas.json_normalize(
#     data,
#     record_path=['students'],
#     meta=[
#         'class',
#         ['info', 'president'],
#         ['info', 'contacts', 'tel']    # 展示的数据层级以列表形式
#     ]
# )
# print(df4)


# 读取内嵌数据中的一组数据
# glom 模块来处理数据套嵌，glom 模块允许我们使用 . 来访问内嵌对象的属性
# value = glom(data, 'a.b.c')
df5 = pandas.read_json('nested_deep.json')
# print(df5)
col: Series = df5['students']
print(col)
math: Series = col.apply(lambda row: glom(row, 'grade.math'))
print(math)























