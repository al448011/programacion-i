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


coche = Coche()
coche.acelerar(100)
coche.actualizar(1.5)
coche.decelerar(40.1)
coche.actualizar(0.5)

print(f'Tiempo: {coche.consultar_tiempo()}')
print(f'Distancia: {coche.consultar_distancia()}')
print(f'Velocidad actual: {coche.consultar_velocidad_actual()}')
print(f'Velocidad media: {coche.consultar_velocidad_media()}')