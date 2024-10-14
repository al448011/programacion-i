from math import sqrt

a = int(input('Introduce a: '))
b = int(input('Introduce b: '))
c = int(input('Introduce c: '))

x1 = (-b + sqrt(b**2 - 4 * a * c))/ (2 * a)
x2 = (-b - sqrt(b**2 - 4 * a * c))/ (2 * a)

print(f'x1 = {float(x1)}\nx2 = {float(x2)}')