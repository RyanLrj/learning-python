"""
use radius to calculate circumference and area

version: 1.1
Author: Ryan
"""
import math

radius = float(input('radius:'))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'{circumference = :.1f}')
print(f'{area = :.1f}')
