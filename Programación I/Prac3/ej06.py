def contar_divisores(n):
    cont = 1
    num_divisores = 0

    while cont <= n:
        if n % cont == 0:
            num_divisores += 1
        cont += 1

    return num_divisores


# --- Programa principal ---
n = int(input('Introduce un número entero: '))
print(f'El número {n} tiene {contar_divisores(n)} divisores')
