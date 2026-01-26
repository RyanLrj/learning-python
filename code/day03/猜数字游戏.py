"""
猜数字游戏

version: 1.0
author: Ryan
"""
import random

answer = random.randrange(1,101)
counter = 0
while True:
    counter += 1
    num = int(input('answer='))
    if num < answer:
        print('too small')
    elif num > answer:
        print('too big')
    else:
        print('right')
        break
print(f'一共猜了{counter}次')