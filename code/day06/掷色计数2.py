"""
投掷5000次色子计算各面出现次数

version: 2.0
author: Ryan
"""

import random

counters = [0] * 6
#模拟掷色子计算每点出现的次数
for i in range(5000):
    face = random.randrange(1,7)
    counters[face-1] += 1
#输出各点数出现次数
for face in range(1 , 7):
    print(f'{face}点数出现的次数为{counters[face-1]}次')