class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def reintegrar(self, cantidad):
        self.saldo -= cantidad

    def consultar_saldo(self):
        return self.saldo


c1 = Cuenta(0)
c2 = Cuenta(1000)

c1.ingresar(100)
c2.reintegrar(20)

print(f'Saldos: {c1.consultar_saldo()} y {c2.consultar_saldo()}')