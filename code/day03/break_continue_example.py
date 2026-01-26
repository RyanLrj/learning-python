"""
从1到100的偶数求和(break_continue)

version: 1.0
author: Ryan
"""
total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)