def todos_dígitos(cadena):
    for caracter in cadena:
        if not caracter.isdigit():
            return False
    return True

nombre_fichero = input('Introduce el nombre de un fichero: ')

with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
    contenido = fichero.read()

palabras = contenido.split()

for palabra in palabras:
    if todos_dígitos(palabra):
        print(palabra)
