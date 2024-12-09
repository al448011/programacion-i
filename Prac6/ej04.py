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


fichero = input('Introduce el nombre de un fichero de test: ')

with open(fichero, 'r') as fichero:
    plantilla = fichero.readline()[:-1]
    número_total_de_preguntas = len(plantilla)

    for línea in fichero:
        if línea[-1] == '\n':
            línea = línea[:-1]

        alumno = línea.split('#')
        respuestas = evaluación_test(plantilla, alumno[1])

        aciertos = respuestas[0]
        fallos = respuestas[1]

        nota = 10 * (aciertos - fallos) / número_total_de_preguntas

        if nota < 5:
            print(f'DNI: {alumno[0]} NOTA: NO APTO')
        else:
            print(f'DNI: {alumno[0]} NOTA: APTO ({nota:5.2f})')
