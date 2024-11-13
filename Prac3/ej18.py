cadena = input('Introduce una cadena de caracteres: ')

todos = 0
posicion_caracter = 0
primer_caracter = 0
posicion_primer_caracter = 0
suma_cadena = 0

for caracter in cadena:
    if not caracter.isdigit():
        todos = 1
        if primer_caracter == 0:
            posicion_primer_caracter = posicion_caracter
            primer_caracter = caracter
    else:
        suma_cadena += int(caracter)

    posicion_caracter += 1

if todos == 0:
    print('Todos los caracteres son dígitos')
    print(f'¿Cuántos dígitos? {len(cadena)}')
    print(f'¿Suma de dígitos? {suma_cadena}')
else:
    print(f'Primer "no dígito": \'{primer_caracter}\' en posición {posicion_primer_caracter}')