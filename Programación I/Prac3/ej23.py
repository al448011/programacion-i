cadena_a = input('Introduce una cadena de caracteres A: ')
cadena_b = input('Introduce una cadena de caracteres B: ')

if len(cadena_b) == 0:
    print('B es sufijo de A')
elif cadena_b in cadena_a:
    print('B es sufijo de A')
elif len(cadena_b) > len(cadena_a):
    print('B no es sufijo de A')
else:
    print('B no es sufijo de a')