def evaluación_test(plantilla, respuestas):
    if len(respuestas) != len(plantilla):
        return None

    num_pregunta = 0
    bien = 0
    mal = 0
    ns = 0

    for correcta in plantilla:
        if respuestas[num_pregunta] == plantilla[num_pregunta]:
            bien += 1
        elif respuestas[num_pregunta] == '*':
            ns += 1
        else:
            mal += 1

        num_pregunta += 1

    return [bien, mal, ns]


plantilla = input('Introduce la plantilla de respuestas correctas: ')
print('Ve introduciendo respuestas de alumnos, o vacío para acabar...')
respuestas = input('Nuevas respuestas: ')

cont_alumnos = 0

while len(respuestas) != 0:

    if len(respuestas) != len(plantilla):
        print(f'La cadena introducida es de longitud {len(respuestas)} (se esperaba {len(plantilla)})')
        respuestas = input('Nuevas respuestas: ')
    else:
        resultados = evaluación_test(plantilla,respuestas)

        cont_alumnos += 1

        print(f'Resultados: {resultados[0]} BIEN; {resultados[1]} MAL; {resultados[2]} NS/NC')
        respuestas = input('Nuevas respuestas: ')

print(f'Alumnos corregidos: {cont_alumnos}')
