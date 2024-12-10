from moduloimagen import leerImagen, mostrarImagen


def nueva_matriz(fila, columna, valor_inicial):
    matriz = []

    for i in range(fila):
        matriz.append(columna * [valor_inicial])

    return matriz


def promedio_entorno(matriz, fila, columna):
    suma = 0
    for i in range(fila - 1, fila + 2):
        for j in range(columna - 1, columna + 2):
            if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]):
                suma += matriz[i][j]

    valor_medio = suma / 9

    return valor_medio


def difuminada(matriz, num):
    filas = len(matriz)
    columnas = len(matriz[0])
    ultimate_matriz = nueva_matriz(len(matriz), len(matriz[0]), 0)

    for fila in range(filas):
        for columna in range(columnas):
            if fila == 0 or fila == len(matriz) - 1 or columna == 0 or columna == len(matriz[fila]) - 1:
                ultimate_matriz[fila][columna] = num
            else:
                ultimate_matriz[fila][columna] = round(promedio_entorno(matriz, fila, columna))

    return ultimate_matriz


imagen = input('Introduce el nombre de la imagen: ')
matriz = leerImagen(imagen)

num = int(input('Introduce el valor del borde: '))
difuminada = difuminada(matriz, num)

mostrarImagen(difuminada)