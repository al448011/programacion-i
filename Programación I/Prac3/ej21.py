cadena_original = input('Introduce una cadena de caracteres: ')

inicio = 0

while inicio < len(cadena_original) and (cadena_original[inicio] == ' ' or cadena_original[inicio] == '-'):
    inicio += 1

fin = len(cadena_original)

while fin > 0 and (cadena_original[fin - 1] == ' ' or cadena_original[fin - 1] == '-'):
    fin -= 1

cadena_limpia = cadena_original[inicio:fin]

print(f'Cadena limpiada: =>{cadena_limpia}<=')
print(f'Cadena original: =>{cadena_original}<=')