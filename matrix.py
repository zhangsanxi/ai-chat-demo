import numpy as np
m = np.array([
    [1,2,3],
    [4,5,6]
])
print("矩阵:")
print(m)
print("形状:",m.shape)

a = np.array([[1, 2], [3, 4]]) 
b = np.array([[5, 6], [7, 8]])
print("\n矩阵乘法:")
print(a @ b)     #@是矩阵乘法运算符

print("\n全0:")
print(np.zeros((2,3)))
print("\n全1:")
print(np.ones((2, 3)))
print("\n随机数:")
print(np.random.rand(2, 3))    # 2行3列，0~1 之间的随机数