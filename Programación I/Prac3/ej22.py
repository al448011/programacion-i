respuestas_correctas = input('Introduce la plantilla de respuestas correctas: ')

print('Ve introduciendo respuestas de alumnos, o vacío para acabar...')

cont_alumnos = 0

respuesta_alumno = input('Nuevas respuestas: ')

while len(respuesta_alumno) != 0:
    num_pregunta = 0

    bien = 0
    mal = 0
    ns = 0

    if len(respuesta_alumno) != len(respuestas_correctas):
        print(f'La cadena introducida es de longitud {len(respuesta_alumno)} (se esperaba {len(respuestas_correctas)})')
        respuesta_alumno = input('Nuevas respuestas: ')
    else:
        for pregunta in respuesta_alumno:
            if respuesta_alumno[num_pregunta] == respuestas_correctas[num_pregunta]:
                bien += 1
            elif respuesta_alumno[num_pregunta] == '*':
                ns += 1
            else:
                mal += 1

            num_pregunta += 1

        cont_alumnos += 1

        print(f'Resultados: {bien} BIEN; {mal} MAL; {ns} NS/NC')
        respuesta_alumno = input('Nuevas respuestas: ')

print(f'Alumnos corregidos: {cont_alumnos}')