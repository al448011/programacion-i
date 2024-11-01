def es_triángulo(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


def tipo_triángulo(a, b, c):
    if es_triángulo(a, b, c):
        if a == b == c:
            return 'equilátero'
        elif (a == b) and (a != c) or (a == c) and (a != b) or (b == c) and (b != a):
            return 'isósceles'
        elif (a != b) and (a != c) and (b != c):
            return 'escaleno'
    else:
        return None


# --- Programa principal ---

a = int(input('Introduce el lado a: '))
b = int(input('Introduce el lado b: '))
c = int(input('Introduce el lado c: '))

while es_triángulo(a, b, c) is False:
    print('No es un triángulo')
    a = int(input('Introduce el lado a: '))
    b = int(input('Introduce el lado b: '))
    c = int(input('Introduce el lado c: '))
else:
    print(f'Es {tipo_triángulo(a,b,c)}')
