from modulomatrices import leerMatrizEnteros, mostrarMatriz

def sumar_encima_diagonal(matriz):
    if len(matriz) != len(matriz[0]):
        return None

    suma = 0
    
    for fila in range(len(matriz)):
        for columna in range(fila + 1, len(matriz)):
            suma += matriz[fila][columna]

    return suma


fichero = input('Introduce el nombre de un fichero: ')
matriz = leerMatrizEnteros(fichero)

resultado = sumar_encima_diagonal(matriz)

if resultado is None:
    print("Error. Se requiere una matriz cuadrada")
else:
    print(f"La suma de los elementos por encima de la diagonal principal es {resultado}")
