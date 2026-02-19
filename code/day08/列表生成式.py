items = []
for i in range(1,100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)

items = [i for i in range(1,100) if i % 3 == 0 or i % 5 == 0]
print(items)
########
num1 = [1,2,3,4,5,6]
num2 = []
for num in num1:
    num2.append(num ** 2)
print(num2)

num1 = [1,2,3,4,5,6]
num2 = [num ** 2 for num in num1]
print(num2)
########
num1 = [23,34,56,67,78]
num2=[]
for num in num1:
    if num >50:
       num2.append(num)
print(num2)

num1 = [23,34,56,67,78]
num3 = [num for num in num1 if num > 50]
print(num3)
########