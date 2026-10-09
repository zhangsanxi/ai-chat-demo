import pandas as pd
df = pd.read_csv("data.csv")

print("读所有名字")
print(df["姓名"])

print("筛选年龄大于28的人")
print(df["年龄"] > 28)
print(df[df["年龄"] > 28])

print("\n按工资降序:")
print(df.sort_values("工资", ascending=False))


print("\n各城市平均工资:")
print(df.groupby("城市")["工资"].mean())