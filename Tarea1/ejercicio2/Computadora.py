class Computadora:
    # Constructor 1: con todos los datos
    def __init__(self, marca=None, procesador=None, ram=0, almacenamiento=0):
        if marca is None:
            # Constructor 2: valores por defecto
            self.marca = "Sin marca"
            self.procesador = "Sin procesador"
            self.ram = 0
            self.almacenamiento = 0
        else:
            self.marca = marca
            self.procesador = procesador
            self.ram = ram
            self.almacenamiento = almacenamiento

    # Métodos para asignar valores (setters)
    def set_marca(self, marca):
        self.marca = marca

    def set_procesador(self, procesador):
        self.procesador = procesador

    def set_ram(self, ram):
        self.ram = ram

    def set_almacenamiento(self, almacenamiento):
        self.almacenamiento = almacenamiento

    # Métodos para obtener valores (getters)
    def get_ram(self):
        return self.ram

    def get_almacenamiento(self):
        return self.almacenamiento

    # b) Comparar si la RAM es igual a X
    def ram_igual_a(self, x):
        return self.ram == x

    # Mostrar todos los datos
    def mostrar_datos(self):
        print(f"Marca: {self.marca}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")
        print(f"Almacenamiento: {self.almacenamiento} GB")

if __name__ == "__main__":
    # a) Instanciar de 2 objetos 
    #objeto1
    pc1 = Computadora("Lenovo", "Intel i7", 16, 512)
    #objeto2
    pc2 = Computadora()
    pc2.set_marca("HP")
    pc2.set_procesador("AMD Ryzen 5")
    pc2.set_ram(8)
    pc2.set_almacenamiento(1024)

    # b)  Determinar si la cantidad de memoria RAM es igual a X.
    x = 16
    print(f"¿PC1 tiene {x} GB de RAM? {pc1.ram_igual_a(x)}")
    print(f"¿PC2 tiene {x} GB de RAM? {pc2.ram_igual_a(x)}")

    # c)De 2 computadoras, mostrar los datos de la que tiene mayor capacidad de
    #almacenamiento
    print(" Computadora con mayor almacenamiento")
    if pc1.get_almacenamiento() > pc2.get_almacenamiento():
        pc1.mostrar_datos()
    elif pc2.get_almacenamiento() > pc1.get_almacenamiento():
        pc2.mostrar_datos()
    else:
        print("Ambas tienen igual almacenamiento:")
        pc1.mostrar_datos()