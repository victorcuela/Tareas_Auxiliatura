class Bus:
    def __init__(self, capacidad_total):
        self.capacidad_total = capacidad_total
        self.pasajeros_actuales = 0
        self.precio_pasaje = 1.50  # precio fijo dado
    # a) Al bus desean subir X cantidad de pasajeros, actualiza los datos del bus
    def subir_pasajeros(self, cantidad):
        asientos_libres = self.capacidad_total - self.pasajeros_actuales
        if cantidad <= asientos_libres:
            self.pasajeros_actuales = self.pasajeros_actuales + cantidad
            print(f" Subieron {cantidad} pasajeros")
        else:
            print(f" Solo entran {asientos_libres} personas más")
            self.pasajeros_actuales = self.capacidad_total

    # b) Crea un método para cobrar pasaje a los pasajeros. 
    def cobrar_pasaje(self):
        total = self.pasajeros_actuales * self.precio_pasaje
        print(f" Total recaudado: {total} Bs.")

    # c)  Muestra cuántos asientos quedan disponibles
    def asientos_disponibles(self):
        libres = self.capacidad_total - self.pasajeros_actuales
        print(f" Asientos disponibles: {libres}")
    # d) Mostrar estado del bus
    def estado_bus(self):
        print(f"Pasajeros a bordo: {self.pasajeros_actuales} / {self.capacidad_total}")
        self.asientos_disponibles()
# Veamos todo
if __name__ == "__main__":
    mi_bus = Bus(30)
    print("Estado inicial del bus ")
    mi_bus.estado_bus()

    print(" Suben pasajeros ")
    mi_bus.subir_pasajeros(10)
    mi_bus.subir_pasajeros(5)

    print(" Cobro de pasajes -")
    mi_bus.cobrar_pasaje()

    print(" Asientos libres")
    mi_bus.asientos_disponibles()

    print(" Intentar llenar el bus ")
    mi_bus.subir_pasajeros(20)  # no entran todos
    mi_bus.estado_bus()
    mi_bus.cobrar_pasaje()