cadena = input('Introduce una cadena de caracteres: ')

todos = 0

for caracter in cadena:
    if not caracter.isdigit():
        todos = 1


if todos == 0:
    print('Todos los caracteres son dígitos')
else:
    print('No todos los caracteres son dígitos')