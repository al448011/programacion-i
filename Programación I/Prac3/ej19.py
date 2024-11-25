cadena = input('Ve introduciendo palabras, o vacío para acabar...\nNueva Palabra: ')

while len(cadena) != 0:

    es_castellano = True
    caracter_erroneo = 0

    for caracter in cadena:
        if not ('a' <= caracter.lower() <= 'z' or caracter.lower() in 'ñáéíóúü'):
            es_castellano = False
            if caracter_erroneo == 0:
                caracter_erroneo = caracter

    if es_castellano:
        print('Podría ser una palabra correcta')
    else:
        print(f'Contiene un carácter que no es del alfabeto castellano: \'{caracter_erroneo}\'')

    cadena = input('Nueva palabra: ')

print('¡Adiós!')