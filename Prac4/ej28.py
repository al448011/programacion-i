from moduloimagen import leerImagen, mostrarImagen

def nueva_matriz(fila, columna, valor_inicial):

    matriz = []

    for i in range(fila):
        matriz.append(columna * [valor_inicial])

    return matriz

def binarizada(matriz, umbral):

    ultimate_matriz = nueva_matriz(len(matriz), len(matriz[0]), 0)

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] <= umbral:
                ultimate_matriz[fila][columna] = 0
            else:
                ultimate_matriz[fila][columna] = 255

    return ultimate_matriz

imagen = input('Introduce el nombre de la imagen: ')
matriz = leerImagen(imagen)
umbral = int(input('Introduce el umbral: '))
mostrarImagen(binarizada(matriz, umbral))