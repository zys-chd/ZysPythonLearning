"""
numpy learning file for zys
"""


# To start up,import numpy as np

import numpy as np

# one of the most important class in numpy:ndarray
# to create a ndarray use
# numpy.array(object,dtype=None,copy=True,order=None,subok=False,ndmin=0)
# object:对象 数组或嵌套的数列
# dtype:数组元素的数据类型
# copy:数据是否需要复制
# order:数组的样式,C为行方向,F为列方向,A为任意方向(默认)
# subok:默认返回一个与基类类型一致的数组
# ndmin:指定生成数组的最小维度
def ClassOne():
    a=np.array([1,2,3]) # simply create a ndarray
    print(a);print("")
    b=np.array([[1,2,3],[1,2,3]]) # create a 2d ndarray
    print(b);print("")
    c=np.array([1,2,3,4,5,6],ndmin=2) # give a min nd
    print(c);print("")
    d=np.array([1,2,3],dtype=complex) # give the data type
    print(d);print("")
# ClassOne()

# dtype in numpy
# bool_ int_ intc intp int8 ...
# b	布尔型
# i	(有符号) 整型
# u	无符号整型 integer
# f	浮点型
# c	复数浮点型
# m	timedelta（时间间隔）
# M	datetime（日期时间）
# O	(Python) 对象
# S, a	(byte-)字符串
# U	Unicode
# V	原始数据 (void)
def ClassTwo():
    dt=np.dtype(np.int32)
    print(dt);print("")
    dt = np.dtype('i4') # 'i1' 'i2' 'i4' 'i8' -> int8 int16 int32 int64
    print(dt);print("")
    dt = np.dtype([('age',np.int8)])
    print(type(dt))
    student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
    a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
    print(a)

ClassTwo()

"""
MyMatrix=np.eye(5,dtype=np.int32)
MyMatrix2=np.arange(10,dtype=np.int32)
a=np.ones((5,4))
print(a.dtype)
print(a)
print(MyMatrix)
print(MyMatrix.dtype)
print(MyMatrix2.dtype)

b=np.random.randn(5,4)
print(b,b.dtype)
"""