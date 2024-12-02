class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def reintegrar(self, cantidad):
        self.saldo -= cantidad

    def consultar_saldo(self):
        return self.saldo


saldo_inicial = float(input('Introduce cuántos euros quieres como saldo inicial de tu cuenta: '))
persona = Cuenta(saldo_inicial)

opción = 0

while opción != 4:
    print('\n1. Hacer un ingreso\n2. Pedir un reintegro\n3. Consultar el saldo\n4. Salir')
    opción = int(input('Elige una opción: '))

    if opción == 1:
        cantidad = float(input('Introduce cuántos euros quieres ingresar: '))
        persona.ingresar(cantidad)
    elif opción == 2:
        cantidad = float(input('Introduce cuántos euros quieres que se te reintegren: '))
        persona.reintegrar(cantidad)
    elif opción == 3:
        print(f'El saldo actual es {persona.consultar_saldo():.2f} euros')
    elif opción == 4:
        print('¡Adiós!')
