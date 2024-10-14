from math import sin,pi

lado1 = int(input('Introduce el primer lado: '))
lado2 = int(input('Introduce el segundo lado: '))
angulo = int(input('Introduce el ángulo (en grados): '))

area = ((lado1 * lado2) / 2 ) * sin((angulo * pi) / 180)

print(f'El área del triángulo es: {area:.2f}')