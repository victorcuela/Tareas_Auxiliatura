# CLASE PADRE
class Vehiculo:
    def __init__(self, *args):
        if len(args) == 0:
            self.color = "Blanco"
            self.gasolina = 0.0
        elif len(args) == 1:
            self.color = args[0]
            self.gasolina = 0.0
        elif len(args) == 2:
            self.color = args[0]
            self.gasolina = args[1]
    def __str__(self):
        return f"Vehículo → Color: {self.color} | Gasolina: {self.gasolina} litros"
# CLASE HIJA 
class Auto(Vehiculo):
    def __init__(self, *args):
        super().__init__(*args)
    def __iadd__(self, valor):
        if valor == 1:  # auto += 1
            self.gasolina += 5
        return self
    def __add__(self, otro):
        if isinstance(otro, str):
            return Auto(otro, self.gasolina)
        return self
    def __sub__(self, otro):
        if isinstance(otro, Auto):
            return self.gasolina + otro.gasolina
        return 0
    def __str__(self):
        return f"Auto → Color: {self.color} | Gasolina: {self.gasolina} litros"
# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    # Instanciar 2 objetos con diferentes constructores
    auto1 = Auto()                
    auto2 = Auto("Rojo", 20)        
    print(" OBJETOS CREADOS")
    print(auto1)
    print(auto2)
    print() 
    
    print(" APLICAR ++ (+5 LITROS)")
    auto1 += 1
    auto2 += 1
    print(f"auto1 tras ++: {auto1}")
    print(f"auto2 tras ++: {auto2}")
    print()
    # d) Cambiar color del auto
    print(" CAMBIAR COLOR DEL AUTO")
    auto1_nuevo = auto1 + "Azul"
    print(f"Original: {auto1}")
    print(f"Nuevo:    {auto1_nuevo}")
    print()
    #  e) Sumar gasolinaentre los 2 autos
    print(" TOTAL DE GASOLINA ")
    total = auto1 - auto2
    print(f"Total entre los 2 autos: {total} litros")