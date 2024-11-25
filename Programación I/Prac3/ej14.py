cadena = input('Introduce un texto (vacío para acabar): ')

cadena_larga = cadena
cadena_corta = cadena

if len(cadena) == 0:
    print('No se ha introducido ningún texto')
else:
    while len(cadena) > 0:
        if len(cadena) >= len(cadena_larga):
            cadena_larga = cadena
        elif len(cadena) <= len(cadena_corta):
            cadena_corta = cadena

        cadena = input('Introduce otro texto (vacío para acabar): ')

    print(f'Última cadena de mínima longitud, {len(cadena_corta)}: =>{cadena_corta}<=')
    print(f'Última cadena de máxima longitud, {len(cadena_larga)}: =>{cadena_larga}<=')