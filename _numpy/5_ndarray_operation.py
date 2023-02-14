
# 运算
import numpy as np
from numpy import array



# 逻辑运算

stock_change = np.random.normal(0, 1, (8, 10))
# print('stock_change------------\n', stock_change)
stock_c: array = stock_change[0:3, 0:3]
print('stock_c---------------\n', stock_c)
# print(stock_c > 1)  # 元素大于1的为True   np.array 可以与 数值进行比较，实际是其元素的比较，而list不能与数值比较

# stock_c[stock_c > 1] = 2    # 所有大于1的元素设为2
# print(stock_c)


# 通用判断函数     类似于python内置函数 all()  any()
# 所有条件满足则返回True
# print(np.all(stock_c > 0))
# 只要有一个条件满足则返回True
# print(np.any(stock_c > 0))



# 三目运算符
# np.where(stock_c > 0, 1, 0)   满足条件的元素赋值为1， 不满足条件的 赋值为0
# np.logical_and()    # 逻辑与
# np.logical_or()     # 逻辑或
# stock_d = np.where(np.logical_and(stock_c > 0.5, stock_c < 1), 111, 222)
# print(stock_d)
# stock_e = np.where(np.logical_or(stock_c > 0.5, stock_c < 0.2), 111, 222)
# print(stock_e)


# 统计运算
# 统计指标
# axis=1表示按行，axis=0表示按列，不指定axis则是在所有元素中计算求取
# print('max------\n', np.max(stock_c, axis=1))
# print('min------\n', np.min(stock_c, axis=0))
# print('mean------\n', np.mean(stock_c))
# print('median------\n', np.median(stock_c, axis=0))
# print('std------\n', np.std(stock_c, axis=1))
# print('var------\n', np.var(stock_c, axis=1))

# print(stock_c.max())   # 取所有元素中的最大值
# print(stock_c.max(axis=1))   # 取每一行中的最大值
# print(stock_c.max(axis=0))   # 取每一列中的最大值
# print('mean----------\n', stock_c.mean())
# print('std----------\n', stock_c.std())
# print('var----------\n', stock_c.var())


print(stock_c.argmax())   # 最大值的索引(指的是所有元素依次顺序排时的位置)
print(stock_c.argmax(axis=1))   # 每一行中最大值的索引
print(stock_c.argmax(axis=0))   # 每一列中最大值的索引
print(stock_c.argmin(axis=0))   # 每一列中最小值的索引




