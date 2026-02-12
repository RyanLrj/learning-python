"""
列表切片索引计算示例

version: 1.0
author: Ryan
"""

items1 = ['apple', 'banana', 'cherry','dog','eight']

print(items1[2])
print(items1[0])
print(items1[-1])

#start值为0时，使用切片运算符时可以省略.end值为N时，stride值为1时都可将其省略
print(items1[1:4:2])
print(items1[-1:-4:-1])
print(items1[::])


