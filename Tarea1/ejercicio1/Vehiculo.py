class Vehiculo:
    def __init__(self, marca, modelo, anio, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.color = "Verdee" 

    # a) Mostrar kilometraje  y metros
    def mostrar_kilometraje(self):
        km = self.kilometraje
        metros = self.kilometraje * 1000
        print(f"Kilometraje: {km} km")
        print(f"En metros: {metros} m")

    # b) Cambiar color
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print(f"Color cambiado a: {nuevo_color}")
# c) Crear 2 autos
if __name__ == "__main__":
    auto1 = Vehiculo("Toyota", "Corolla", 2020, 45)
    auto2 = Vehiculo("Ford", "Fiesta", 2022, 28)

    print(" Auto 1 ")
    auto1.cambiar_color("Rojo")
    auto1.mostrar_kilometraje()

    print(" Auto 2")
    auto2.cambiar_color("Azul")
    auto2.mostrar_kilometraje()