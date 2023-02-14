import numpy
from matplotlib import pyplot

# 创建画布
pyplot.figure(figsize=(20, 8), dpi=100)

# 散点图
# 房屋面积数据
# x = [225.98, 247.07, 253.14, 457.85, 241.58, 301.01, 20.67, 288.64,
# 163.56, 120.06, 207.83, 342.75, 147.9 , 53.06, 224.72, 29.51,
# 21.61, 483.21, 245.25, 399.25, 343.35]
# 房屋价格数据
# y = [196.63, 203.88, 210.75, 372.74, 202.41, 247.61, 24.9 , 239.34,
# 140.32, 104.15, 176.84, 288.23, 128.79, 49.64, 191.74, 33.1 ,
# 30.74, 400.02, 205.35, 330.64, 283.45]
# pyplot.scatter(x=x, y=y)


# 柱状图
# 电影名字
# movie_name = ['雷神3：诸神黄昏','正义联盟','东方快车谋杀案','寻梦环游记','全球风暴','降魔传','追捕','七十七天','密战','狂兽','其它']
# # 横坐标(必须为数字)
# x = range(len(movie_name))
# # 票房数据
# y = [73853,57767,22354,15969,14839,8725,8716,8318,7916,6764,52222]
# """
# x : 横坐标序列
# height: 柱高-与x对应的用来表示柱高的序列,长度跟x要一致
# width : 柱状图的宽度
# align : 每个柱状图的位置对齐方式 {‘center’, ‘edge’}, optional, default: ‘center’
# **kwargs : color:选择柱状图的颜色
# """
# pyplot.bar(x, height=y, width=0.5, align='center', color=['b','r','g','y','c','m','y','k','c','g','b'])
# # 修改x轴的刻度显示
# pyplot.xticks(x, movie_name, fontsize=16)
# # 添加网格
# pyplot.grid(linestyle='-', alpha=0.8)
# # 添加标题
# pyplot.title('电影票房收入对比')


# 直方图(在某个区间的频次)
# 随机生成（10000,）服从正态分布的数据
# data = numpy.random.randn(10000)
# """
# data:必选参数，绘图数据
# bins:直方图的长条形数目，可选项，默认为10
# facecolor:长条形的颜色
# edgecolor:长条形边框的颜色
# alpha:透明度
# """
# pyplot.hist(x=data, bins=40, facecolor="blue", edgecolor="black", alpha=0.7)
# # 显示横/纵轴标签
# pyplot.xlabel('区间', fontsize=16)
# pyplot.ylabel('频数/频率', fontsize=16)
# # 显示图标题
# pyplot.title("频数/频率分布直方图",fontsize=20)


# 饼图
# label_list = ["第一部分", "第二部分", "第三部分"]  # 各部分标签
# data = [55, 35, 10]  # 各部分大小
# color = ["red", "green", "blue"]  # 各部分颜色
# explode = [0.05, 0, 0]  # 各部分突出值
# """
# x:数量序列，自动算百分比
# labels:设置各部分标签的序列,长度与x一致
# autopct:占比数据显示格式 指定%1.2f%%
# colors:每部分颜色
# explode：设置各部分突出
# labeldistance:设置标签文本距圆心位置，1.1表示1.1倍半径
# autopct：设置圆里面文本
# shadow：设置是否有阴影
# startangle：起始角度，默认从0开始逆时针转
# pctdistance：设置圆内文本距圆心距离
# textprops ：设置标签（labels）和比例文字的格式；字典类型，可选参数，默认值为：None。
# 返回值
# l_text：圆内部文本，matplotlib.text.Text object
# p_text：圆外部文本
# """
# patches, l_text, p_text = pyplot.pie(data, explode=explode, colors=color, labels=label_list, labeldistance=1.1,
#                                      autopct="%1.2f%%", shadow=False, startangle=90, pctdistance=0.6,
#                                      textprops={'fontsize': 20, 'color': 'black'})
# pyplot.axis('equal')  # 设置横轴和纵轴大小相等，这样饼才是圆的
# pyplot.legend(loc='upper right', fontsize=16)  # 设置图例


# 条形图
label_list = ['2014', '2015', '2016', '2017']  # 横坐标刻度显示值
num_list1 = [20, 30, 15, 35]  # 纵坐标值1
num_list2 = [15, 30, 40, 20]  # 纵坐标值2
x1 = range(len(num_list1))
x2 = [i + 0.4 for i in x1]
num_list3 = [10, 20, 30, 40, 50]

rects1 = pyplot.bar(x1, height=num_list1, width=0.4, alpha=0.8, color='red', label="一部门")
rects2 = pyplot.bar(x2, height=num_list2, width=0.4, color='green', label="二部门")
pyplot.yticks(num_list3,fontsize=16)   # y轴取值范围
pyplot.ylabel("数量",fontsize=16)

pyplot.xticks([index + 0.2 for index in x1], label_list,fontsize=16)
pyplot.xlabel("年份",fontsize=16)
pyplot.title("圆梦公司",fontsize=20)
# 编辑文本
for rect in rects1:
    height = rect.get_height()
    pyplot.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom",fontsize=16)
for rect in rects2:
    height = rect.get_height()
    pyplot.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom",fontsize=16)
# 添加网格显示
pyplot.grid(True, linestyle="--", alpha=0.5)
# 添加图例
pyplot.legend(loc=0,fontsize=16)





pyplot.show()
