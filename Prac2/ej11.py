angulo = int(input('Introduce un ángulo (en grados): '))

if angulo == 0:
    print('Nulo')

if 0 < angulo < 90:
    print('Agudo')

if angulo == 90:
    print('Recto')

if 90 < angulo < 180:
    print('Obtuso')

if angulo == 180:
    print('Llano')

if 180 < angulo < 360:
    print('Cóncavo')

if angulo == 360:
    print('Completo')
