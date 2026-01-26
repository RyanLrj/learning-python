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

#引入continue

total = 0
i = 2
for i in range (1,101):
    if i % 2 == 0:
        continue
    total += i
print(total)