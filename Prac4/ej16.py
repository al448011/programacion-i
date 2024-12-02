def es_dígito(carácter):
    if carácter.isdigit():
        return True
    else:
        return False

def secuencias_dígitos(cadena):

    dígito = ''
    lista_secuencias = []

    for carácter in cadena:
        if es_dígito(carácter):
            dígito += carácter
        else:
            if len(dígito) > 0:
                lista_secuencias.append(dígito)
            dígito = ''

    if len(dígito) > 0:
        lista_secuencias.append(dígito)

    return lista_secuencias

cadena = input('Introduce una cadena: ')
lista_secuencias = secuencias_dígitos(cadena)

print(f'La lista de secuencias obtenida es {lista_secuencias}')
