from moduloimagen import leerImagen, mostrarImagen


def aplicar_filtro_negativo(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    for fila in range(num_filas):
        for columna in range(num_columnas):
            matriz[fila][columna] = 255 - matriz[fila][columna]


fichero = input('Introduce el nombre de la imagen: ')
matriz = leerImagen(fichero)

aplicar_filtro_negativo(matriz)

mostrarImagen(matriz)
