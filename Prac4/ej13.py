print('Ve introduciendo candidaturas, o vacío para acabar...')
candidatura = input('Nueva candidatura: ')

lista_candidatura = []

while len(candidatura) != 0:
    lista_candidatura += [candidatura]
    candidatura = input('Nueva candidatura: ')

lista_votos = []

for candidatura in lista_candidatura:
    votos_candidatura = input(f'Votos para {candidatura}: ')
    lista_votos += [int(votos_candidatura)]

votos_totales = 0

for votos in lista_votos:
    votos_totales += votos

for i in range(len(lista_candidatura)):
    print(f'{lista_votos[i] / votos_totales * 100:.2f}% de los votos a candidaturas para {lista_candidatura[i]}')