# ndarray对象的内容可以通过索引或切片来访问和修改，与 Python 中 list 的切片操作一样。
# ndarray 数组可以基于 0 - n 的下标进行索引，切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，从原数组中切割出一个新数组。


import numpy as np

# 一、数组索引切片

# stock_change = np.random.normal(0, 1, (8, 10))
# print(stock_change)

# 索引取数组的子数组或元素
# sub_arr1 = stock_change[0, 3]   # 第1行、第4列
# sub_arr2 = stock_change[0][3]   # 第1行、第4列
# print(sub_arr1 == sub_arr2)   # True
# print('sub_arr----------\n', sub_arr1)
# print('sub_arr----------\n', sub_arr2)
# sub_arr3 = stock_change[0:3, 2:5]   # 前3行、第3~5列  注意切片左闭右开
# sub_arr4 = stock_change[0:3][2:5]   # 此写法不可!!!，这实际是先[0:3]切片，对其结果再进行[2, 5]切片，很容易越界；
# print(sub_arr3 == sub_arr4)    # False
# print('sub_arr----------\n', sub_arr3)
# print('sub_arr----------\n', sub_arr4)



# 二、形状修改
# stock_change2 = np.random.normal(0, 1, (4, 5))
# print(stock_change2)
# res1 = stock_change2.reshape([5, 4])   # 将原来20个元素按顺序一个一个排成5行4列，打破原有形状
# print(res1)
# res2 = stock_change2.reshape([-1, 10])   # 不确定行数(待算出)，列数为10，自动计算出行数为2，若无法整除则报错
# print(res2)
# stock_change2.resize([5, 4])   # resize与reshape作用相同，只是resize操作原数据，而reshape返回操作结果，原数据不改变
# print(stock_change2)

# res3 = stock_change2.T    # 矩阵转置
# print(res3)



# 三、类型修改
# arr1 = stock_change2.astype(np.int32)     # 元素由浮点型转为整型
# print(arr1)

# arr2 = stock_change2.tostring()       # 元素由数字转为bytes字符串(tostring逐渐弃用)
# arr2 = stock_change2.tobytes()       # 元素由数字转为bytes字符串
# print(arr2)



# 四、数组去重
temp = np.array([[1, 2, 3, 4], [2, 2, 4, 5]])
temp2 = np.array([[1, 2, 3, 4], [2, 2, 3, 4, 5]])   # !!!注意创建array时，不要这样创建！二维的元素长度不一样，数据类型即是object
arr3 = np.unique(temp)
print(arr3)
