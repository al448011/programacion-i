nombre_fichero = input('Introduce el nombre de un fichero: ')

fichero = open(nombre_fichero, 'r')

dígitos = 0
letras = 0

línea = fichero.readline()
while línea != '':
    for caracter in línea:
        if caracter.isdigit():
            dígitos += 1
        elif caracter.lower() in ['a-z']:
            letras += 1

fichero.close()

print(f'Dígitos decimales: {dígitos}')
print(f'Letras del inglés: {letras}')
