import numpy as np

# 矩阵的基本知识
# 乘法、求逆、转置等
# 加法： 对应位置相加
# 乘法： 标量和每个位置的元素相乘
# 矩阵向量（矩阵）乘法[*****]    [M行, N列]*[N行, L列] = [M行, L列]


# numpy数组的运算
# 数组与数的运算
# arr = np.array([1, 2, 3, 4])
# 数组和数字直接可以进行运算
# print(arr + 1)
# print(arr / 2)


# 数组与数组的运算需要满足广播机制：
# 1.维度相同 或者 2.两个数组对应的维度中，有一个为1，即是两个数组的shape元祖中，相同位置的两个数至少有一个为1
# 例如
# 数组A         9 ✖ ️1 ✖ 7 ✖ 1
# 数组B              8 ✖ 1 ✖ 5
# 运算结果       9 ✖ 8 ✖ 7 ✖ 5
arr1 = np.array([[1, 2, 3], [2, 3, 4]])
arr2 = np.array([[4, 2, 3], [5, 2, 1]])
# np.array: [[1 + 4, 2 + 2, 3 + 3],
#           [2 + 5, 3 + 2, 4 + 1]]
# print(arr1 + arr2)

arr3 = np.array([[1, 2, 3, 2, 1, 4], [5, 6, 1, 2, 3, 1]])
arr4 = np.array([[1], [3]])
# np.array: [[1 + 1, 2 + 1, 3 + 1, 2 + 1, 1 + 1, 4 + 1],
#           [5 + 3, 6 + 3, 1 + 3, 2 + 3, 3 + 3, 1 + 3]]
# print(arr3 + arr4)

# 数组乘法
# np.matmul() 与 np.dot() 实现数组相乘，两者进行矩阵相乘时，没有区别，但dot支持矩阵与数字相乘，matmul不支持
# arr5 = np.array([[80, 86], [82, 80], [85, 78], [90, 90], [86, 82], [82, 90], [78, 80], [92, 94]])
# arr6 = np.array([[0.7], [0.3]])
# print('arr5--------------\n', arr5)
# print('arr6--------------\n', arr6)
# res1 = np.matmul(arr5, arr6)
# print('res1--------------\n', res1)
# res2 = np.dot(arr5, arr6)
# print(res2)
# print(res1 == res2)


# Numpy matrices必须是2维的,但是 numpy arrays (ndarrays) 可以是多维的（1D，2D，3D····ND）. Matrix是Array的一个小的分支，包含于Array。所以matrix 拥有array的所有特性
# 在numpy中matrix的主要优势是：
# （1）相对简单的乘法运算符号。
matrix1 = np.mat('4 3; 2 1')
matrix2 = np.mat('1 2; 3 4')
# print(matrix1)
# print(matrix2)
print('矩阵相乘----\n', matrix1 * matrix2)   # 数学矩阵相乘
# （2）matrix 和 array 都可以通过objects后面加.T.T 得到其转置。
# 但是 matrix objects 还可以在后面加 .H.H得到共轭矩阵, 加 .I.I 得到逆矩阵。
# 相反的是在numpy里面arrays遵从逐个元素的运算，所以array：c和d进行c∗d运算相当于对应的元素相乘
arr7 = np.array([[4, 3], [2, 1]])
arr8 = np.array([[1, 2], [3, 4]])
print('numpy数组相乘----\n', arr7 * arr8)    # 对应元素相乘

# ∗∗ 运算符的作用也不一样
print('矩阵相乘----a∗a-----\n', matrix1 ** 2)
print('元素逐个求平方--------\n', arr7 ** 2)







