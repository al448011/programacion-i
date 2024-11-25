from modulomatrices import leerMatrizEnteros


def sumar_columna(matriz, columna):
    suma_elementos = 0
    for fila in range(len(matriz)):
        suma_elementos += matriz[fila][columna]
    return suma_elementos


fichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(fichero)

for columna in range(len(matriz[0])):
    print(f'La suma de los elementos en la columna {columna} es {sumar_columna(matriz, columna)}')