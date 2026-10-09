import pandas as pd

# 读取 CSV
df = pd.read_csv("data.csv")

print("完整数据:")
print(df)

print("\n前 2 行:")
print(df.head(2))

print("\n年龄平均值:", df["年龄"].mean())
print("最高年龄:", df["年龄"].max())