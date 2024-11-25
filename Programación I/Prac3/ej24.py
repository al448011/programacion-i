print('Ve introduciendo cadenas de caracteres, o vacío para acabar...')

cadena = input('Nueva cadena: ')

while len(cadena) != 0:
    secuencias = 0
    en_secuencia = False

    for caracter in cadena:
        if caracter.isdigit():
            if not en_secuencia:
                secuencias += 1
                en_secuencia = True
        else:
            en_secuencia = False

    print(f'Secuencias de dígitos encontradas: {secuencias}')
    cadena = input('Nueva cadena: ')

print('¡Adiós!')