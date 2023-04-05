import numpy
import numpy as np

# Arrny = [2, 1, 5, 8, 6]
# x = numpy.array(Arrny)
# print(x)
# print(x.dtype)
# 2
# # 使用列表输出二维数组
# date = [[1, 2], [3, 4], [5, 6]]
# y = numpy.array(date)
# print(y)  # 打印二维数组
# print(y.ndim)  # 打印数组维度
# print(y.shape)
# # 使用zero/ones/empty创建数组，根据shape来创建
# c = numpy.zeros(6)  # 创建一个含有6个元素的一维数组 元素全为0
# print(c)
# d = numpy.zeros((3, 2))  # 创建一个三行两列的二维数组，内部元素全为0
# print(d)
# d = numpy.ones((2, 3))  # 创建一个二行三列的二维数组，内部元素的全为1
# print(d)
# d = numpy.empty((4, 5))  # 创建一个四行五列的未被的初始化数组
# print(d)
z = np.ones([3, 2], dtype=int)
print(z)
usual_numpy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
x = np.asarray(usual_numpy)
print(x)
print(x.shape)
y = x.reshape(2, 7)  # 数组改变形状
print(y)
print(y.shape)
c = np.matmul(z, y)
print(c)

