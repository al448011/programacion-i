def leer_entero_mayor_que(n):
    a = int(input(f'Introduce un entero mayor que {n}: '))

    while a <= n:
        a = int(input(f'Esperaba entero mayor que {n} y {a} no lo es. Dame otro: '))

    return a

def contar_divisores(n):
    cont = 1
    num_divisores = 0

    while cont <= n:
        if n % cont == 0:
            num_divisores += 1
        cont += 1

    return num_divisores

def es_primo(n):
    if contar_divisores(n) == 2:
        return True
    else:
        return False

a = leer_entero_mayor_que(0)
b = leer_entero_mayor_que(a)

print(f'Voy a buscar primos entre {a} y {b}...')
print('Encontrados:', end=' ')

cont = a
cont_primos = 0

while cont <= b:
    if es_primo(cont):
        print(cont, end=' ')
        cont_primos += 1
    cont += 1

if cont_primos == 0:
    print('ninguno')