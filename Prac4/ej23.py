from modulomatrices import leerMatrizEnteros, mostrarMatriz


def producto_diagonal_secundaria(matriz):

    if len(matriz) != len(matriz[0]):
        print('Error. Se requiere una matriz cuadrada')
        return None

    for i in range(len(matriz)):
        aux = matriz[i]
        matriz[i] = matriz[len(matriz) - 1]
        matriz[len(matriz) - 1 - i] = aux

    mostrarMatriz(matriz)

    #return producto

fichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(fichero)
mostrarMatriz(matriz)
print(f'\n\n')
producto_diagonal_secundaria(matriz)