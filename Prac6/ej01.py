fichero = input('Introduce el nombre de un fichero: ')

with open(fichero, 'r') as fichero:
    línea = fichero.readline()

    decimales = 0
    letras = 0

    while línea != '':
        for caracter in línea:
            if 'a' <= caracter.lower() <= 'z':
                letras += 1
            elif caracter.isdigit():
                decimales += 1

        línea = fichero.readline()

print(f'Dígitos decimales: {decimales}')
print(f'Letras del inglés: {letras}')
