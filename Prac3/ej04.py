def calcular_cadena_repetida(c, n, s):
    return (c + s) * (n-1) + c


# --- Programa principal ---
cadena = str(input('Introduce una cadena: '))
separador = str(input('Introduce un separador: '))
repeticiones = int(input('Introduce un máximo de repeticiones: '))

for i in range(1, repeticiones+1):
    print(calcular_cadena_repetida(cadena, i, separador))
