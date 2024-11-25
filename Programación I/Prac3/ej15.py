cadena_a = input('Introduce A: ')
cadena_b = input('Introduce B: ')

c = cadena_a + cadena_b
r = c * int(cadena_b)
s = int(r) + int(cadena_a)

print(f'C, concatenación de A y B: {c}')
print(f'R, repetición de C un número B de veces: {r}')
print(f'S, suma de los números representados por R y A: {s}')