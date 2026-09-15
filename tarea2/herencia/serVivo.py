# CLASE PADRE PRINCIPAL
class ServVivo:
    def __init__(self, nombre, edad, salud):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Salud: {self.salud}")
# NIVEL 1 Animal
class Animal(ServVivo):
    def __init__(self, nombre, edad, salud, tipo_alimento, lugar):
        super().__init__(nombre, edad, salud)
        self.tipo_alimento = tipo_alimento
        self.lugar = lugar
    def mostrar(self):
        super().mostrar()
        print(f"Come: {self.tipo_alimento}")
        print(f"Vive en: {self.lugar}")
# NIVEL 1 Planta
class Planta(ServVivo):
    def __init__(self, nombre, edad, salud, tipo, alto):
        super().__init__(nombre, edad, salud)
        self.tipo = tipo
        self.alto = alto
    def mostrar(self):
        super().mostrar()
        print(f"Especie: {self.tipo}")
        print(f"Altura: {self.alto} metros")
# NIVEL 2  Reptil
class Reptil(Animal):
    def __init__(self, nombre, edad, salud, piel):
        super().__init__(nombre, edad, salud, "carnívoro", "tierra")
        self.piel = piel
    def mostrar(self):
        super().mostrar()
        print(f"Tipo de piel: {self.piel}")
# NIVEL 3  Víbora
class Vivora(Reptil):
    def __init__(self, nombre, edad, salud, piel, veneno):
        super().__init__(nombre, edad, salud, piel)
        self.veneno = veneno
    def mostrar(self):
        super().mostrar()
        print(f"Es venenosa: {self.veneno}")
        print("-" * 30)
# NIVEL 2  Felino
class Felino(Animal):
    def __init__(self, nombre, edad, salud, pelaje):
        super().__init__(nombre, edad, salud, "carnívoro", "selva")
        self.pelaje = pelaje

    def mostrar(self):
        super().mostrar()
        print(f"Pelaje: {self.pelaje}")
# NIVEL 3 León
class Leon(Felino):
    def __init__(self, nombre, edad, salud, pelaje, melena):
        super().__init__(nombre, edad, salud, pelaje)
        self.melena = melena
    def mostrar(self):
        super().mostrar()
        print(f"Tiene melena: {self.melena}")
        print("-" * 30)
# NIVEL 3  Gato
class Gato(Felino):
    def __init__(self, nombre, edad, salud, pelaje, raza):
        super().__init__(nombre, edad, salud, pelaje)
        self.raza = raza
    def mostrar(self):
        super().mostrar()
        print(f"Raza: {self.raza}")
        print("-" * 30)
# NIVEL 2  Roedor
class Roedor(Animal):
    def __init__(self, nombre, edad, salud, dientes):
        super().__init__(nombre, edad, salud, "herbívoro", "tierra")
        self.dientes = dientes

    def mostrar(self):
        super().mostrar()
        print(f"Dientes: {self.dientes}")
# NIVEL 3 Ratón
class Raton(Roedor):
    def __init__(self, nombre, edad, salud, dientes, color):
        super().__init__(nombre, edad, salud, dientes)
        self.color = color

    def mostrar(self):
        super().mostrar()
        print(f"Color: {self.color}")
        print("-" * 30)
# NIVEL 2  Humano
class Humano(Animal):
    def __init__(self, nombre, edad, salud, pais):
        super().__init__(nombre, edad, salud, "omnívoro", "ciudad")
        self.pais = pais

    def mostrar(self):
        super().mostrar()
        print(f"País: {self.pais}")
# NIVEL 3  Niño
class Nino(Humano):
    def __init__(self, nombre, edad, salud, pais, escuela):
        super().__init__(nombre, edad, salud, pais)
        self.escuela = escuela

    def mostrar(self):
        super().mostrar()
        print(f"Va a la escuela: {self.escuela}")
        print("-" * 30)
# NIVEL 3  Adulto
class Adulto(Humano):
    def __init__(self, nombre, edad, salud, pais, trabajo):
        super().__init__(nombre, edad, salud, pais)
        self.trabajo = trabajo
    def mostrar(self):
        super().mostrar()
        print(f"Trabajo de: {self.trabajo}")
        print("-" * 30)
# NIVEL 3  Anciano
class Anciano(Humano):
    def __init__(self, nombre, edad, salud, pais, jubilado):
        super().__init__(nombre, edad, salud, pais)
        self.jubilado = jubilado
    def mostrar(self):
        super().mostrar()
        print(f"Es jubilado: {self.jubilado}")
        print("-" * 30)
# NIVEL 2  Flor
class Flor(Planta):
    def __init__(self, nombre, edad, salud, tipo, alto, color):
        super().__init__(nombre, edad, salud, tipo, alto)
        self.color = color
    def mostrar(self):
        super().mostrar()
        print(f"Color de flor: {self.color}")
        print("-" * 30)
# NIVEL 2 Conejo
class Conejo(Animal):
    def __init__(self, nombre, edad, salud, orejas):
        super().__init__(nombre, edad, salud, "hierba", "bosque")
        self.orejas = orejas
    def mostrar(self):
        super().mostrar()
        print(f"Tamaño de orejas: {self.orejas}")
        print("-" * 30)
# NIVEL 2  Rana
class Rana(Animal):
    def __init__(self, nombre, edad, salud, color_piel):
        super().__init__(nombre, edad, salud, "insectos", "agua")
        self.color_piel = color_piel
    def mostrar(self):
        super().mostrar()
        print(f"Color de piel: {self.color_piel}")
        print("-" * 30)

# PROGRAMA PRINCIPAL 
print("====EJERCICIO DE HERENCIA====\n")

# Creamos objetos
leoncito = Leon("Simba", 7, "buena", "amarillo", "si")
gatito = Gato("Mishi", 3, "excelente", "gris", "común")
vibora = Vivora("Vivora", 10, "buena", "escamosa", "si")
ratonc = Raton("Mickey", 1, "buena", "afilados", "blanco")
conejito = Conejo("Bugs", 5, "buena", "largas")
ranita = Rana("Ranita", 2, "buena", "verde")
ninito = Nino("Pedro", 8, "muy buena", "Bolivia", "San José")
adulto = Adulto("Luis", 35, "regular", "Bolivia", "profesor")
abuelo = Anciano("Juan", 75, "regular", "Bolivia", "si")
florcita = Flor("Rosa", 1, "viva", "ornamental", 0.5, "roja")
# Mostramos datos
leoncito.mostrar()
gatito.mostrar()
vibora.mostrar()
ratonc.mostrar()
conejito.mostrar()
ranita.mostrar()
ninito.mostrar()
adulto.mostrar()
abuelo.mostrar()
florcita.mostrar()

print("\n===FIN ===")