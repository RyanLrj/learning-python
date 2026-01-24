"""
BMI calculator

version: 1.0
Author: Ryan
"""

height = float(input('height(cm):'))
weight = float(input('weight(kg):'))

BMI = weight / (height/100) ** 2
print(f'{BMI = :.1f}')
if BMI < 18.5:
    print('you are too thin')
elif BMI >= 18.5 and BMI <= 25:
    print('you are fit')
elif BMI >= 25:
    print('you are too heavy')
