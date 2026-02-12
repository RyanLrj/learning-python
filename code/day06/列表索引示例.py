"""
列表索引示例

version: 1.0
author: Ryan
"""
from unicodedata import digit

items1 = ['apple', 'banana', 'cherry']
print(items1[2])
print(items1[0])
print(items1[-1])

items1[2] = 'dog'
print(items1)
items1[-1] = 'eight'
print(items1)