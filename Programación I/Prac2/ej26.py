n = int(input('Introduce un número entero: '))

cont = 1
cont_divisores = 0

while cont <= n:
    if n % cont == 0:
        cont_divisores += 1
    cont += 1

if cont_divisores == 2:
    print("Es primo")
else:
    print("No es primo")