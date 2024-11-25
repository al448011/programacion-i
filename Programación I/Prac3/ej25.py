def contar_secuencias_dígitos(cadena):
    secuencias = 0
    en_secuencia = False

    for caracter in cadena:
        if caracter.isdigit():
            if not en_secuencia:
                secuencias += 1
                en_secuencia = True
        else:
            en_secuencia = False
    return secuencias

print('Ve introduciendo cadenas de caracteres, o vacío para acabar...')

cadena = input('Nueva cadena: ')

while len(cadena) != 0:
    print(f'Secuencias de dígitos encontradas: {contar_secuencias_dígitos(cadena)}')
    cadena = input('Nueva cadena: ')

print('¡Adiós!')