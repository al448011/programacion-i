a = int(input('Introduce el lado a: '))
b = int(input('Introduce el lado b: '))
c = int(input('Introduce el lado c: '))

if (a == b) and (a != c) or (a == c) and (a != b) or (b == c) and (b != a):
    print('Es isósceles')
else:
    print('No es isósceles')
