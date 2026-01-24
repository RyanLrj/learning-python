"""
计算三角形周长面积

version: 1.0
author: Ryan
"""

a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'周长：{perimeter}')
    print(f'面积：{s}')
else :
    print('不能构成三角形')
