def posición_menor(lista, inicio):
    posición_mínimo = inicio

    for i in range(inicio, len(lista)):
        if lista[i] < lista[posición_mínimo]:
            posición_mínimo = i

    return posición_mínimo


def intercambiar(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def ordenar_lista(lista):
    for i in range(len(lista)):
        índice_menor = posición_menor(lista, i)

        intercambiar(lista, i, índice_menor)


nombre_fichero = input('Introduce el nombre de un fichero de test: ')

lista_dni = []

with open(nombre_fichero, 'r') as fichero_entrada:
    plantilla = fichero_entrada.readline()[:-1]

    for línea in fichero_entrada:
        if línea[-1] == '\n':
            línea = línea[:-1]

        alumno = línea.split('#')
        lista_dni.append(alumno[0])

    ordenar_lista(lista_dni)
    for i in range(len(lista_dni)):
        print(lista_dni[i])
