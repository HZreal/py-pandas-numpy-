# NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。
# ndarray 对象是用于存放同类型元素的多维数组。
# ndarray 中的每个元素在内存中都有相同存储大小的区域。
# ndarray 内部由以下内容组成：
# 一个指向数据（内存或内存映射文件中的一块数据）的指针。
# 数据类型或 dtype，描述在数组中的固定大小值的格子。
# 一个表示数组形状（shape）的元组，表示各维度大小的元组。
# 一个跨度元组（stride），其中的整数指的是为了前进到当前维度下一个元素需要"跨过"的字节数。

import numpy as np


# 一、numpy.array数组对象
# ndarry1 = np.array([1, 2, 3], dtype=None, copy=True, order=None)
# print(ndarry1)
# ndarry2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(ndarry2)
# ndarry3 = np.array([1, 2, 3, 4, 5], ndmin=3)     # 指定最小维度
# print(ndarry3)
# ndarry4 = np.array([1, 2, 3], dtype=complex)     # 指定数据类型为复数
# print(ndarry4)

# NumPy 数组的维数称为秩（rank），秩就是轴的数量，即数组的维度，一维数组的秩为 1，二维数组的秩为 2，以此类推。
# 在 NumPy中，每一个线性的数组称为是一个轴（axis），也就是维度（dimensions）。比如说，二维数组相当于是两个一维数组，其中第一个一维数组中每个元素又是一个一维数组。所以一维数组就是 NumPy 中的轴（axis），第一个轴相当于是底层数组，第二个轴是底层数组里的数组。而轴的数量——秩，就是数组的维数。
# 很多时候可以声明 axis。axis=0，表示沿着第 0 轴进行操作，即对每一列进行操作；axis=1，表示沿着第1轴进行操作，即对每一行进行操
# narray = np.array([1, 2, 3])
# narray = np.array([[1, 2, 3], [4, 5, 6]])
# narray = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]], [[4, 5, 6], [5, 6, 7], [6, 7, 8]], [[7, 8, 9], [8, 9, 10], [9, 10, 11]]])
# print('narray--------', narray)
# print('ndim--数组维数(秩)-----------', narray.ndim)
# print('shape--数组维度，对于矩阵n行m列-----------', narray.shape)
# print('size--元素个数n*m-----------', narray.size)
# print('dtype--元素类型-----------', narray.dtype)
# print('itemsize--每个元素大小，以字节为单位-----------', narray.itemsize)
# print('flags--内存信息-----------', narray.flags)
# print('real--实部-----------', narray.real)
# print('imag--虚部----------', narray.imag)
# print('data------------', narray.data)



# 二、numpy.dtype数据类型，用来描述与数组对应的内存区域是如何使用，它描述了数据的以下几个方面：：
# 数据的类型（整数，浮点数或者 Python 对象）
# 数据的大小（例如， 整数使用多少个字节存储）
# 数据的字节顺序（小端法或大端法）
# 在结构化类型的情况下，字段的名称、每个字段的数据类型和每个字段所取的内存块的部分
# 如果数据类型是子数组，那么它的形状和数据类型是什么
# # dtype 对象构造
# np.dtype(object, align=None, copy=None)
# # 使用标量类型
# dt1 = np.dtype(np.int32)
# print('dt1-----------------', dt1)
# # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
# # float16, float32, float64 四种数据类型可以使用字符串 'f2','f4','f8' 代替
# dt2 = np.dtype('i4')
# print('dt2-----------------', dt2)
# # 字节顺序标注
# dt3 = np.dtype('<i4')    # 字节顺序是通过对数据类型预先设定 < 或 > 来决定的。 < 意味着小端法(最小值存储在最小的地址，即低位组放在最前面)。> 意味着大端法(最重要的字节存储在最小的地址，即高位组放在最前面)
# print('dt3-----------------', dt3)
# # 首先创建结构化数据类型
# dt4 = np.dtype([('age', np.int8)])
# print('dt4-----------------', dt4)

# # 将数据类型 dtype 应用于 ndarray 对象
# ndarry5 = np.array([(10,), (20,), (30,)], dtype=dt4)
# print(ndarry5)
# # 类型字段名可以用于存取实际的 age 列
# ndarry6 = np.array([(10,), (20,), (30,)], dtype=dt4)
# print(ndarry6['age'])
#
# # 定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象
# student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
# print('student struct---------------', student)
# ndarry7 = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
# print(ndarry7)




# 三、ndarray数组的创建方式(除了上述ndarray类构造创建外)
# 1、empty/zeros/ones
# numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
# empty1 = np.empty(shape=[3, 2], dtype=int, order='C')   # C、F分别表示行优先、列优先
# print('empty1--------------------\n', empty1)
# numpy.zeros 创建指定大小的数组，数组元素以 0 来填充
# zeros1 = np.zeros(shape=5)  # 默认为浮点数类型
# print('zero1--------------------\n', zeros1)
# zeros2 = np.zeros((3, 4), dtype=np.int)
# print('zero2--------------------\n', zeros2)
# zeros3 = np.zeros((2, 3), dtype=[('x', 'i4'), ('y', 'i4')])
# print('zero3--------------------\n', zeros3)
# numpy.ones 创建指定形状的数组，数组元素以 1 来填充
# np.ones(shape=[2, 4], dtype=None, order='C')
# ones1 = np.ones(5)
# print('one1--------------------\n', ones1)
# ones2 = np.ones([2, 2], dtype=int)
# print('one2--------------------\n', ones2)
# 将元素1全部改为元素0
# zz0 = np.zeros_like(ones2)
# print('one2 所有元素转为0 --------------------\n', zz0)

# 2、asarray/array
# numpy.asarray 类似于 numpy.array，
# numpy.asarray 参数只有三个，比 numpy.array 少两个。
# numpy.asarray 为浅拷贝； numpy.array 为深拷贝
# np.asarray([], dtype=None, order=None)
# tmp = np.array([[1, 2, 3], [4, 5, 6]])
# arr1 = np.array(tmp)     # 深拷贝，原数据修改，对自己不影响
# asarr1 = np.asarray(tmp)
# print(arr1, asarr1, sep='\n')
# # 修改tmp
# tmp[0, 0] = 100
# print(arr1, asarr1, sep='\n')

# 3、arange/linspace/logspace
# NumPy 从固定数值范围创建一维数组
# numpy.arange 创建数值范围内的等步长的一维数组
# np.arange(start, stop, step, dtype)
ndarry11 = np.arange(start=10, stop=20, step=2)
print('生成一维数组，从10开始到20，每间隔2生成一个----------------', ndarry11)
# numpy.linspace 用于创建一个一维数组，数组是一个等差数列构成的
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
ndarry22 = np.linspace(start=1, stop=10, num=10)
print('生成一维数组，从1开始到10，生成个数为10个----------------', ndarry22)
# numpy.logspace 函数用于创建一个于等比数列
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)  默认底数base是10
ndarry33 = np.logspace(1.0, 2.0, num=8)
print('生成一维数组，底数为10，指数从1.0到2.0，生成8个----------------', ndarry33)
ndarry44 = np.logspace(0, 9, 10, base=2.0)
print('生成一维数组，底数为2.0，指数从0到9，生成10个----------------', ndarry44)

# 4、frombuffer/fromiter
# numpy.frombuffer 用于实现动态数组。接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象
# numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
# asarr2 = np.frombuffer('hello world'.encode(), dtype='S1')
# print(asarr2)
# numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。
# numpy.fromiter(iterable, dtype, count=-1)
# 使用迭代器创建 ndarray
# asarr3 = np.fromiter(iter(range(5)), dtype=float)
# print(asarr3)






