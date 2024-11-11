def todos_dígitos(cadena):
    for caracter in cadena:
        if not caracter.isdigit():
            return False
    return True


cadena = input('Introduce una cadena de caracteres: ')

if todos_dígitos(cadena):
    print('Todos los caracteres son dígitos')
else:
    print('No todos los caracteres son dígitos')
