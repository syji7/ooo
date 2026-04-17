# 导包
import numpy as np

#  1. 使用 np.array() 从列表创建一维数组 [1, 2, 3, 4, 5]
a1 = np.array([1, 2, 3, 4, 5])
print(a1)
# 2. 使用 np.zeros() 创建 3行4列 的全0数组
a2 = np.zeros((3, 4))
print(a2)
# 3. 使用 np.ones() 创建 2行3列 的全1数组
a3 = np.ones((2, 3))
print(a3)
# 4. 使用 np.arange() 创建从0到10(不包含10)，步长为2的数组
a4 = np.arange(0, 10, 2)
print(a4)
# 5. 使用 np.linspace() 创建从0到1，包含10个等间距点的数
a5 = np.linspace(0, 1, 10)
print(a5)

print('==========================================')

# 1. 创建 2x2 的单位矩阵（对角线为1，其余为0）
print(np.eye(2, 2))
a6 = np.array([[1, 0], [0, 1]])
print(a6)
# 2. 创建元素全为 5 的 3x3 数组
a7 = np.full((3, 3), 5)
# 3. 创建随机数组，范围0-1，形状为 2x3
a8 = np.random.rand(2, 3)  # 0到1之间的随机数
print(a8)
a9 = np.random.randn(2, 3)  # 0之间的正太随机数
print(a9)
a10 = np.random.randint(1, 10, (3, 4))  # 范围内的随机数和形状
print(a10)
print('==========================================')
a1 = np.array([1, 2, 3, 4, 5])
# 1. 打印数组的维度数(ndim)
print(a1.ndim)
# 2. 打印数组的形状(shape)
print(a1.shape)
# 3. 打印数组的元素总数(size)
print(a1.size)
# 4. 打印数组的数据类型(dtype)
print(a1.dtype)
print('==========================================')
arr = np.arange(1, 13)
print(arr)
# 1. 将 arr 重塑为 2行6列 的二维数组
print(arr.reshape(2, 6))
# 2. 将 arr 重塑为 2x2x3 的三维数组
print(arr.reshape(2, 2, 3))  # 就是说三维数组就是三个括号
# 3. 将上面的三维数组展平为一维数组（使用 flatten）
print(arr.flatten())
# 4. 使用 ravel() 展平数组
print(arr.ravel())
# 5. 获取数组的转置
print(arr.T)  # 一列数组的转置就是它自己
print('==========================================')

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# 1. 计算 a + b
print(a + b)
# 2. 计算 a - b
print(a - b)
# 3. 计算 a * b （对应位置相乘）
print(a * b)
# 4. 计算 a / b
print(a / b)
# 5. 计算 a ** 2 （平方）
print(a ** 2)
# 6. 判断 a > 2，返回布尔数组
print(a > 2)
print('==========================================')
arr = np.array([10, 20, 30, 40])

# 1. 数组每个元素加 5

# 2. 数组每个元素乘以 2

# 3. 数组每个元素除以 10

# 矩阵乘法详解：@, *, dot, matmul 的区别
print('\n========== @, *, dot, matmul 的区别 ==========')

# 准备数据
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

print("数组 a:")
print(a)
print("\n数组 b:")
print(b)

# 1. * 运算符：元素级乘法（Hadamard积）
result_multiply = a * b
print("\n1. a * b (元素级乘法):")
print(result_multiply)
print("解释：对应位置相乘 [[1*5, 2*6], [3*7, 4*8]]")

# 2. dot() 方法：点积/矩阵乘法
result_dot = np.dot(a, b)
print("\n2. np.dot(a, b) (矩阵乘法):")
print(result_dot)
print("解释：行乘列求和 [[1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]]")

# 3. @ 运算符：矩阵乘法（Python 3.5+）
result_at = a @ b
print("\n3. a @ b (矩阵乘法运算符):")
print(result_at)
print("解释：与 dot 相同，是矩阵乘法的语法糖")

# 4. matmul() 函数：矩阵乘法
result_matmul = np.matmul(a, b)
print("\n4. np.matmul(a, b) (矩阵乘法函数):")
print(result_matmul)
print("解释：与 @ 和 dot 基本相同")

# 验证 @, dot, matmul 的等价性
print("\n========== 验证等价性 ==========")
print(f"@ == dot: {np.array_equal(result_at, result_dot)}")
print(f"@ == matmul: {np.array_equal(result_at, result_matmul)}")
print(f"dot == matmul: {np.array_equal(result_dot, result_matmul)}")

# 关键区别示例
print("\n========== 关键区别示例 ==========")

# 区别1: * 与其他三个完全不同
print("1. * 是元素级运算，其他三个是矩阵乘法:")
print(f"   a * b = \n{a * b}")
print(f"   a @ b = \n{a @ b}")

print('===================================')
# 1. 创建向量 v = [1, 2, 3]
v1 = [1, 2, 3]
# 2. 创建 3x2 矩阵 M
v2 = np.array([[1, 2], [3, 4], [5, 6]])
# 3. 计算 v @ M （向量与矩阵相乘）
print(v1 @ v2)

# 广播机制,会自动生成对应相乘
# 创建三行一列的数组
a = np.array([[1], [2], [3]])
print(a)
# 创建一行三列的数组
b = np.array([[1, 2, 3]])
print(b)
print(a + b)
print('======================================')

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# 1. 计算所有元素的和
print(arr.sum())
# 2. 计算所有元素的平均值
print(arr.mean())
# 3. 计算所有元素的最大值
print(np.max(arr))
print(arr.max(axis=1))
# 4. 计算所有元素的最小值
print(np.min(arr))
print(arr.min(axis=1))
# 5. 计算每一列的和（沿axis=0）
print(arr.sum(axis=0))
# 6. 计算每一行的平均值（沿axis=1）
print(arr.sum(axis=1))