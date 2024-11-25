from modulomatrices import leerMatrizEnteros


def sumar_elementos(matriz):

    suma_elementos = 0

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            suma_elementos += matriz[fila][columna]

    return suma_elementos


fichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(fichero)
print(f'La suma de todos los elementos en la matriz es {sumar_elementos(matriz)}')
