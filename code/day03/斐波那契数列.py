"""
输出斐波那契数列中的前20个数

version: 1.0
author: Ryan
"""

a, b = 0, 1
for _ in range (20):
    a, b = b, a + b
    print(a)

