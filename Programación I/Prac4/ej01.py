print('Ve introduciendo cadenas de caracteres, o vacío para acabar...')

lista = []

cadena = input('Nueva cadena: ')

while len(cadena) != 0:
    lista.append(cadena)
    cadena = input('Nueva cadena: ')

print('Cadenas leídas:')

for elemento in lista:
    print(f'Cadena de longitud {len(elemento)}: =>{elemento}<=')