from modulomatrices import leerMatrizEnteros


def sumar_fila(matriz, fila):
    suma_elementos = 0
    for columna in range(len(matriz[fila])):
        suma_elementos += matriz[fila][columna]
    return suma_elementos


fichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(fichero)
for fila in range(len(matriz)):
    print(f'La suma de los elementos en la fila {fila} es {sumar_fila(matriz, fila)}')
