from modulomatrices import leerMatrizEnteros


def promedio_entorno(matriz, fila, columna):

    suma = 0
    for i in range(fila - 1, fila + 2):
        for j in range(columna - 1, columna + 2):
            suma += matriz[i][j]

    valor_medio = suma / 9

    return valor_medio

imagen = input('Introduce el nombre de la imagen: ')
fila = int(input('Introduce un número de fila: '))
columna = int(input('Introduce un número de columna: '))

matriz = leerMatrizEnteros(imagen)
promedio = promedio_entorno(matriz, fila, columna)

print(f'El promedio en el entorno del punto ({fila},{columna}) es {promedio:.2f}')