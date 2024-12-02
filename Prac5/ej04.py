class Coche:
    def __init__(self):
        self.tiempo = 0
        self.distancia = 0
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento

    def decelerar(self, decremento):
        self.velocidad -= decremento

    def actualizar(self, tiempo):
        self.tiempo += tiempo
        self.distancia += self.velocidad * tiempo

    def consultar_tiempo(self):
        return self.tiempo

    def consultar_distancia(self):
        return self.distancia

    def consultar_velocidad_actual(self):
        return self.velocidad

    def consultar_velocidad_media(self):

        if self.tiempo == 0:
            return None
        else:
            velocidad_media = self.distancia / self.tiempo
            return velocidad_media


print('Tu coche está inicialmente parado')
coche = Coche()

opción = 0

while opción != 5:
    print(f'\n1. Acelerar\n2. Decelerar\n3. Actualizar\n4. Consultar\n5. Salir')
    opción = int(input('Elige una opción: '))

    if opción == 1:
        cantidad = float(input('Introduce cuántos km/h quieres acelerar: '))
        coche.acelerar(cantidad)
    elif opción == 2:
        cantidad = float(input('Introduce cuántos km/h quieres decelerar: '))
        coche.decelerar(cantidad)
    elif opción == 3:
        cantidad = float(input('Introduce cuántas horas han pasado: '))
        coche.actualizar(cantidad)
    elif opción == 4:
        print(f'El tiempo trascurrido es {coche.consultar_tiempo():.2f} h')
        print(f'La distancia recorrida es {coche.consultar_distancia():.2f} km')
        print(f'La velocidad actual es {coche.consultar_velocidad_actual():.2f} km/h')
        if coche.consultar_velocidad_media() is None:
            print('No puedo calcular la velocidad media si no ha trascurrido tiempo')
        else:
            print(f'La velocidad media es {coche.consultar_velocidad_media():.2f} km/h')
    elif opción == 5:
        print('¡Adiós!')
