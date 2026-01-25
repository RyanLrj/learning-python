"""
0到100偶数求和

version: 1.0
author: Ryan
"""

total = 0
for _ in range(0,101):
    if _ % 2 == 0:
        total += _
print(total)

#or we can use sum function

print(sum(range(2,101,2)))