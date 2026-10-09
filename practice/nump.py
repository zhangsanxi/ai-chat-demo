import numpy as np
nums = [1,2,3,4,5]
result = []
for n in nums:
    result.append(n+10)
print("列表",result)
# append作用列表的方法，追加一个元素到末尾
a = np.array([1,2,3,4,5])
print("数组:",a + 10)
# np作用方便计算，省略了append和for循环，直接整体执行