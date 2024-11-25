cadena = input('Introduce un texto (vacío para acabar): ')

while len(cadena) > 0:
    print(f'Su longitud es {len(cadena)}')
    cadena = input('Introduce otro texto (vacío para acabar): ')


print('¡Adiós!')