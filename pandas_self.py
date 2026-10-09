import pandas as pd
df = pd.read_csv("data.csv")

print(df[df["城市"] == "深圳"])
print(df.sort_values("年龄",ascending=True))
print(df["工资"].mean())
print(df.groupby("城市").size())