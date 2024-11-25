while True:
    a = int(input('Introduce el lado a: '))
    b = int(input('Introduce el lado b: '))
    c = int(input('Introduce el lado c: '))

    if (a + b > c) and (a + c > b) and (b + c > a):
        if (a == b == c):
            print('Es equilátero')
        elif (a == b) and (a != c) or (a == c) and (a != b) or (b == c) and (b != a):
            print('Es isósceles')
        elif (a != b) and (a != c) and (b != c):
            print('Es escaleno')

        break
    else:
        print('No es un triángulo')