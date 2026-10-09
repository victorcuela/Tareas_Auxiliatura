from abc import ABC, abstractmethod
# Clase Padrek: Animal
class Animal(ABC):
    def __init__(self, edad, peso, especie):
        self._edad = edad
        self._peso = peso
        self._especie = especie
    def get_datos(self):
        return f"Especie: {self._especie}, Edad: {self._edad} años, Peso: {self._peso} kg"
    # c) Método respirar() — general
    def respirar(self):
        return "Toma oxígeno del medio ambiente"
    # d) Método mover() — comportamiento general
    def mover(self):
        return "Se desplaza de un lugar a otro"
# Clase Derivada: Terrestre
class Terrestre(Animal):
    def __init__(self, edad, peso, especie, cantidad_patas, tipo_piel):
        super().__init__(edad, peso, especie)
        self.__cantidad_patas = cantidad_patas
        self.__tipo_piel = tipo_piel

    def get_datos(self):
        return (super().get_datos() +
                f", Patas: {self.__cantidad_patas}, Piel: {self.__tipo_piel}")
    # Métodos propios
    def caminar(self):
        return "Camina usando sus patas por el suelo"

    def hibernar(self):
        return "Duerme durante meses cuando hace frío"

    # c) Sobreescribir respirar
    def respirar(self):
        return " Usa pulmones para respirar aire"

    # d) Sobreescribir mover
    def mover(self):
        return " Se desplaza caminando o corriendo por la tierra"
# Clase Derivada: Aereo
class Aereo(Animal):
    def __init__(self, edad, peso, especie, envergadura, tipo_alas):
        super().__init__(edad, peso, especie)
        self.__envergadura = envergadura
        self.__tipo_alas = tipo_alas
    def get_datos(self):
        return (super().get_datos() +
                f", Envergadura: {self.__envergadura}m, Alas: {self.__tipo_alas}")
    # Métodos propios
    def volar(self):
        return "Se eleva y se mueve por el aire"
    def planear(self):
        return "Se desliza aprovechando las corrientes de aire"
    # c) Sobreescribir respirar
    def respirar(self):
        return " Usa pulmones y sacos aéreos, respira de forma continua"
    # d) Sobreescribir mover
    def mover(self):
        return " Se desplaza volando por el aire"
# Clase Derivada: Acuatico
class Acuatico(Animal):
    def __init__(self, edad, peso, especie, profundidad_max, tipo_agua):
        super().__init__(edad, peso, especie)
        self.__profundidad_max = profundidad_max
        self.__tipo_agua = tipo_agua

    def get_datos(self):
        return (super().get_datos() +
                f", Profundidad máx: {self.__profundidad_max}m, Agua: {self.__tipo_agua}")

    def nadar(self):
        return "Se impulsa moviendo su cuerpo y aletas en el agua"

    def sumergirse(self):
        return "Baja a profundidades bajo el agua"

    # c) Sobreescribir respirar
    def respirar(self):
        return " Toma oxígeno disuelto en el agua usando branquias"

    # d) Sobreescribir mover
    def mover(self):
        return " Se desplaza nadando dentro del agua"
# b) Instanciar objetos y mostrar datos
if __name__ == "__main__":
    print("=" * 60)
    print("            DATOS DE LOS ANIMALES")
    print("=" * 60)

    # Crear objetos
    perro = Terrestre(5, 12.5, "Perro doméstico", 4, "Pelo")
    aguila = Aereo(8, 4.2, "Águila real", 2.3, "Plumón y plumas")
    tiburon = Acuatico(15, 110.0, "Tiburón blanco", 1200, "Salada")

    # Mostrar datos
    print("\n ANIMAL TERRESTRE")
    print(perro.get_datos())
    print(f"Acción: {perro.caminar()}")
    print(f"Respiración: {perro.respirar()}")
    print(f"Movimiento: {perro.mover()}")

    print("\n ANIMAL AÉREO")
    print(aguila.get_datos())
    print(f"Acción: {aguila.volar()}")
    print(f"Respiración: {aguila.respirar()}")
    print(f"Movimiento: {aguila.mover()}")

    print("\n ANIMAL ACUÁTICO")
    print(tiburon.get_datos())
    print(f"Acción: {tiburon.nadar()}")
    print(f"Respiración: {tiburon.respirar()}")
    print(f"Movimiento: {tiburon.mover()}")

    print("\n" + "=" * 60)