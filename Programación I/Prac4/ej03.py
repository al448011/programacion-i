print('Ve introduciendo números enteros positivos, o un número negativo para acabar...')

lista_pares = []
lista_impares = []

num = int(input('Nuevo número: '))

while num >= 0:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    num = int(input('Nuevo número: '))

print(f'Números pares: {lista_pares}')
print(f'Números impares: {lista_impares}')