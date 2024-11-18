print('Ve introduciendo cadenas de caracteres, o vacío para acabar...')

lista = []

cadena = input('Nueva cadena: ')

while len(cadena) != 0:
    lista = [cadena] + lista
    cadena = input('Nueva cadena: ')

print('Cadenas leídas (desde la última hasta la primera):')

for elemento in lista:
    print(f'Cadena de longitud {len(elemento)}: =>{elemento}<=')