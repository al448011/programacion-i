from moduloimagen import leerImagen, mostrarImagen


def reflejar_horizontal(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila]) // 2):
            aux = matriz[fila][columna]
            matriz[fila][columna] = matriz[fila][len(matriz[fila]) - 1 - columna]
            matriz[fila][len(matriz[fila]) - 1 - columna] = aux


imagen = input('Introduce el nombre de la imagen: ')
matriz = leerImagen(imagen)
reflejar_horizontal(matriz)
mostrarImagen(matriz)
