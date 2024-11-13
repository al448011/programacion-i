cadena_original = input('Introduce una cadena de caracteres: ')

cont_espacios = 0


for caracter in cadena_original:
        if caracter == ' ' or caracter == '-':
            cont_espacios += 1

if len(cadena_original) == cont_espacios:
    print(cadena_original)
else:
    print(cadena_original[len(cadena_original) - cont_espacios])