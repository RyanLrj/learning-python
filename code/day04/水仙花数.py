"""
找出100到999范围内的水仙花数

version: 1.0
author: Ryan
"""

for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
        

