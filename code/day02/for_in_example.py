"""
每隔一秒输出一次 'hello world',持续一小时

version；1.0
author: Ryan
"""
import time

for i in range(3600):
    print('hello world')
    time.sleep(1)
