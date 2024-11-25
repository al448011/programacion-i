n = int(input('Introduce un número entero: '))

cont = 1

while cont**2 < n:
    print(f'El cuadrado de {cont} es {cont**2}')
    cont += 1