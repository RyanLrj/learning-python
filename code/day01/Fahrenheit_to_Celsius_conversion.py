"""
将华氏温度转换为摄氏温度

version: 1.0
Author: Ryan
"""

f = float(input('请输入华氏温度'))
c = (f - 32)/ 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
