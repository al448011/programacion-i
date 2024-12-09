fichero = input('Introduce el nombre de un fichero de test: ')

with open(fichero, 'r') as fichero:

    plantilla = fichero.readline()

    for línea in fichero:
        if línea[-1] == '\n':
            línea = línea[:-1]

        alumno = línea.split('#')
        print(f'El alumno con DNI {alumno[0]} ha respondido {alumno[1]}')


print(f'Un alumno perfecto habría respondido {plantilla}')