def es_triángulo(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


# --- Programa principal ---

a = int(input('Introduce el número a: '))
b = int(input('Introduce el número b: '))
c = int(input('Introduce el número c: '))

if es_triángulo(a, b, c):
    print('Es un triángulo')
else:
    print('No es un triángulo')
