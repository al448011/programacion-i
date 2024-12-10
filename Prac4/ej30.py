from moduloimagen import leerImagen, mostrarImagen


def reflejar_vertical(matriz):
    for fila in range(len(matriz) // 2):
        aux = matriz[fila]
        matriz[fila] = matriz[len(matriz) - 1 - fila]
        matriz[len(matriz) - 1 - fila] = aux

imagen = input('Introduce el nombre de la imagen: ')
matriz = leerImagen(imagen)
reflejar_vertical(matriz)
mostrarImagen(matriz)