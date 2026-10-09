import numpy as np

# 模拟一个班的成绩（3 个学生，4 门课）
scores = np.array([
    [90, 85, 88, 92],   # 学生1
    [78, 92, 80, 85],   # 学生2
    [88, 79, 95, 91]    # 学生3
])

print("成绩表:")
print(scores)
print("形状:", scores.shape)

# 1. 每个学生的平均分（按行求平均）
print("\n每个学生平均分:", scores.mean(axis=1))

# 2. 每门课的平均分（按列求平均）
print("每门课平均分:", scores.mean(axis=0))

# 3. 全班最高分
print("全班最高分:", scores.max())