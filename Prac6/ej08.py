nombre_fichero = input('Introduce el nombre de un fichero: ')

with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
    contenido = fichero.read()

palabras = contenido.split()

palabra_mas_larga = ''

for palabra in palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

print(f'Su secuencia de caracteres sin espacios más larga es "{palabra_mas_larga}".')