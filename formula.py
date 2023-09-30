import math
a = float(input('Введите a: '))
b = float(input('Введите  b: '))
z1 = (math.cos(a)-math.cos(b))**2 -(math.sin(a)-math.sin(b))**2
z2 = (math.sin(-4)**2)*((a-b)/2)*(math.cos(a+b))
print(f'z1 = {z1}')
print(f'z2 = {z2}')
