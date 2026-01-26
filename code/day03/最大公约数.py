"""
输入两个正整数求它们的最大公约数

version: 1.0
author: Ryan
"""
a = int(input('请输入第一个正整数：'))
b = int(input('请输入第二个正整数：'))
for i in range(a,0,-1):
    if a % i == 0 and b % i == 0:
        print(f'最大公约数：{i}')
        break