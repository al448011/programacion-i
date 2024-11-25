from modulomatrices import leerMatrizEnteros


def sumar_diagonal(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    if num_filas == num_columnas:
        suma_elementos = 0
        for i in range(len(matriz)):
            suma_elementos += matriz[i][i]
        return suma_elementos
    else:
        return None


fichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(fichero)

suma = sumar_diagonal(matriz)

if suma is None:
    print('Error. Se requiere una matriz cuadrada')
else:
    print(f'La suma de los elementos en la diagonal principal es {suma}')
