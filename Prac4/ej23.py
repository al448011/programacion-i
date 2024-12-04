from modulomatrices import leerMatrizEnteros, mostrarMatriz

def producto_diagonal_secundaria(matriz):
    if len(matriz) != len(matriz[0]):
        return None
    elif len(matriz) == 1:
        producto = matriz[0][0]
        return producto

    producto = 1
    columna = len(matriz) - 1

    for fila in range(len(matriz) -1):
        producto *= matriz[fila][columna]
        columna -= 1

        print(f'{fila=}, {columna=}')

    return producto

# matriz = [[5]]
# print(producto_diagonal_secundaria(matriz))
fichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(fichero)

print(f'El producto de los elementos en la diagonal secundaria es {producto_diagonal_secundaria(matriz)}')