# 维度数组与矩阵运算
# NumPy 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用， 这种组合广泛用于替代 MatLab
# SciPy 是一个开源的 Python 算法库和数学工具包
# SciPy 包含的模块有最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算

# numpy的数组为内存块为一体式存储，针对元素为同类型的数组；而python的list内存块为分离式存储，针对元素数据类型多样化的数组；
# numpy底层实现为C语言，解除了GIL，支持绝对意义上的并行化计算；而python的并行受GIL锁的存在，实际上是时间片轮转

import random
import time
import numpy



# 性能对比（计算时间）
a = [random.random() for i in range(100000000)]

t1 = time.time()
print(t1)
sum1 = sum(a)
t2 = time.time()
print(t2)
print(t2 - t1)

b = numpy.array(a)


t3 = time.time()
print(t3)
sum2 = numpy.sum(b)
t4 = time.time()
print(t4)
print(t4 - t3)















