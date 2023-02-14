# 正态分布Normal distribution
# 均匀分布uniform distribution

from matplotlib import pyplot
import numpy as np

# np.random 随机模块

# 一、均匀分布
# 返回[0.0, 1.0]内一组均匀分布的数
# rand1 = np.random.rand(4)
# print('rand1-----------\n', rand1)
# rand2 = np.random.rand(2, 4)
# print('rand2-----------\n', rand2)

# 从一个均匀分布[low, high)中随机取样，注意是左闭右开，size表示ndarray的shape，为一个元祖(m, n, k)表示m行n列k高...
# uniform1 = np.random.uniform(low=1.0, high=10.0, size=(3, 5))
# print('uniform1-----------\n', uniform1)

# 从一个均匀分布中随机取样，生成一个整数或N维整数数组，取值范围：若high非空，则在[low, high)中随机取整，反之在[0, low)
# randint1 = np.random.randint(low=1, high=2, size=(2, 5), dtype=int)
# print('randint1-----------\n', randint1)

# 生成均匀分布图
# pyplot.figure(figsize=(20, 8), dpi=100)
# x = np.random.uniform(0, 1, 1000)   # 生成1000个[0, 1)的数字
# pyplot.hist(x=x, bins=10, facecolor="blue", edgecolor="red")  # 分成10个区间，
# pyplot.show()



# 二、正态分布
# 均值 μ
# 方差 δ^2   越小，数据越集中，表现的正态分布图为'瘦高'
randn1 = np.random.randn()

# normal1 = np.random.normal(loc=2, scale=0.4, size=100)
# print(normal1)

# standard_normal1 = np.random.standard_normal(size=(3, 4))    # 指定
# print(standard_normal1)

pyplot.figure(figsize=(20, 8), dpi=100)
x = np.random.normal(1.75, 1, 10000000)   # 生成1000个μ=2  δ^2=0.4的点
pyplot.hist(x=x, bins=1000)  #
pyplot.show()




