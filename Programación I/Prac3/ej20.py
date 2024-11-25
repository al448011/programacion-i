def es_letra_castellana(caracter):
    es_castellano = True

    if not ('a' <= caracter.lower() <= 'z' or caracter.lower() in 'ñáéíóúü'):
        es_castellano = False

    return es_castellano

def primer_no_castellano(cadena):
    caracter_erroneo = 0

    for caracter in cadena:
        if not es_letra_castellana(caracter):
            if caracter_erroneo == 0:
                caracter_erroneo = caracter

    if caracter_erroneo == 0:
        return None
    else:
        return caracter_erroneo


cadena = input('Ve introduciendo palabras, o vacío para acabar...\nNueva Palabra: ')

while len(cadena) != 0:

    if primer_no_castellano(cadena) is None:
        print('Podría ser una palabra correcta')
    else:
        print(f'Contiene un carácter que no es del alfabeto castellano: \'{primer_no_castellano(cadena)}\'')

    cadena = input('Nueva palabra: ')

print('¡Adiós!')