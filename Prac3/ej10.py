def sumar_divisores_propios(n):
    suma_divisores = 0

    for divisor in range(1, n):
        if n % divisor == 0:
            suma_divisores += divisor

    return suma_divisores

def son_amigos(a,b):
    if sumar_divisores_propios(a) == b and sumar_divisores_propios(b) == a:
        return True
    else:
        return False

a = int(input('Introduce un número entero a: '))
b = int(input('Introduce un número entero b: '))

seguimos = 'S'

while seguimos == 'S':
    if son_amigos(a,b):
        print('Los dos números son amigos')
    else:
        print('Los dos números no son amigos')

    seguimos = input('¿Seguimos comprobando amistades (S/N)? ')

    if seguimos == 'S':
        a = int(input('Introduce un número entero a: '))
        b = int(input('Introduce un número entero b: '))
    else:
        print('¡Adiós!')