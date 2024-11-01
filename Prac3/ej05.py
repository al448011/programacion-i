def mostrar_cadena_repetida(c, n, s):
    print((c + s) * (n - 1) + c)


# --- Programa principal ---
cadena = str(input('Introduce una cadena: '))
separador = str(input('Introduce un separador: '))
repeticiones = int(input('Introduce un máximo de repeticiones: '))

for i in range(1, repeticiones + 1):
    mostrar_cadena_repetida(cadena, i, separador)
