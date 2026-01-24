"""
百分制成绩换算等级

version: 1.0
author: Ryan
"""

score = float(input('分数：'))
match score:
    case s if s >=90: grade = 'A'
    case s if s >=80: grade = 'B'
    case s if s >=70: grade = 'C'
    case s if s >=60: grade = 'D'
    case _: grade = 'E'
print(f'{grade =}')

