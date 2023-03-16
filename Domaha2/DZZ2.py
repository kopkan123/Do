x = int(input('Введите число x:'))
y = int(input('Введите число y:'))
s = x + y
p = x * y
y1 = int((s + ((-s) ** 2 - 4 * p) ** 0.5) / 2)
x1 = int((s - ((-s) ** 2 - 4 * p) ** 0.5) / 2)
print(x1, y1)   