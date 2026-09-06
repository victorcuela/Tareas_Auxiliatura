class CuentaBancaria:
    def __init__(self, titular, nroCuenta, saldo):
        self.titular = titular
        self.nroCuenta = nroCuenta
        self.saldo = saldo

    #  Depositar y Retirar
    def depositar(self, monto):
        if monto <= 0:  # c) Error si es 0 o negativo
            print("Error: monto no válido")
        else:
            self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:  # b) Saldo insuficiente
            print("Error: no hay suficiente saldo")
        else:
            self.saldo -= monto

    #  Mostrar datos
    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Nº Cuenta: {self.nroCuenta}")
        print(f"Saldo: {self.saldo}")


# Prueba
cuenta = CuentaBancaria("María López", "987654", 300)
cuenta.mostrar()

cuenta.depositar(150)
cuenta.depositar(-20)  # error
cuenta.retirar(100)
cuenta.retirar(600)    # error

cuenta.mostrar()