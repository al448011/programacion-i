from math import pi

def área_círculo(radio):
    return pi * radio ** 2

def longitud_circunferencia(radio):
    return 2 * pi * radio

# --- Programa principal ---
radio = float(input('Introduce el radio: '))
print(f'Área: {área_círculo(radio):.2f}')
print(f'Longitud: {longitud_circunferencia(radio):.2f}')