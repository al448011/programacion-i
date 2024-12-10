from moduloimagen import leerImagen, mostrarImagen

def nueva_matriz(fila, columna, valor_inicial):
    matriz = []

    for i in range(fila):
        matriz.append(columna * [valor_inicial])

    return matriz

def girada_izquierda(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    ultimate_matriz = nueva_matriz(columnas, filas, 0)

    for fila in range(filas):
        for columna in range(columnas):
            ultimate_matriz[columnas - columna - 1][fila] = matriz[fila][columna]

    return ultimate_matriz

imagen = input('Introduce el nombre de la imagen: ')
matriz = leerImagen(imagen)

girada = girada_izquierda(matriz)

mostrarImagen(girada)