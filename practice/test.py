# -*- coding: utf-8 -*-
name = "张三"
age = 20
scores = [90, 89, 88]
person = {"name": "张三", "age": 20}

print(f"{name}今年{age}岁")

for s in scores:
    print(s)

if age >= 18:
    print("成年")
else:
    print("未成年")

def add(a, b):
    return a + b

print(add(3, 5))