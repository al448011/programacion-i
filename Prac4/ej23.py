from modulomatrices import leerMatrizEnteros, mostrarMatriz

def producto_diagonal_secundaria(matriz):
    if len(matriz) != len(matriz[0]):
        return None

    producto = 1
    columna = len(matriz)

    for fila in range(len(matriz)):
        producto *= matriz[fila][columna - 1 - fila]

    return producto


fichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(fichero)

resultado = producto_diagonal_secundaria(matriz)

if resultado is None:
    print('Error. Se requiere una matriz cuadrada')
else:
    print(f'El producto de los elementos en la diagonal secundaria es {resultado}')