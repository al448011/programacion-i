a = int(input('Introduce el lado a: '))
b = int(input('Introduce el lado b: '))
c = int(input('Introduce el lado c: '))

if (a != b) and (a != c) and (b != c):
    print('Es escaleno')
else:
    print('No es escaleno')