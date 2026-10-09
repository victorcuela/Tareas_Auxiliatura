from abc import ABC, abstractmethod
import math
# a) Clase abstracta Figura
class Figura(ABC):
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color
    @abstractmethod
    def obtener_area(self):
        pass
# b) Subclases con método sobrescrito
class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.__lado = lado

    def obtener_area(self):
        return self.__lado * self.__lado
class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def obtener_area(self):
        semi = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return math.sqrt(semi * (semi - self.__lado1) * (semi - self.__lado2) * (semi - self.__lado3))
class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.__radio = radio

    def obtener_area(self):
        return math.pi * self.__radio * self.__radio
# c) y d)
if __name__ == "__main__":
    print("=== Áreas de las figuras ===")
    # 2 objetos de cada clase
    cuad1 = Cuadrado("Rojo", 4)
    cuad2 = Cuadrado("Azul", 6)
    print(f"Cuadrado 1: {cuad1.obtener_area()}")
    print(f"Cuadrado 2: {cuad2.obtener_area()}")

    tri1 = Triangulo("Verde", 3, 4, 5)
    tri2 = Triangulo("Amarillo", 5, 5, 6)
    print(f"Triángulo 1: {tri1.obtener_area()}")
    print(f"Triángulo 2: {tri2.obtener_area()}")

    circ1 = Redondo("Naranja", 3)
    circ2 = Redondo("Morado", 5)
    print(f"Círculo 1: {circ1.obtener_area():.2f}")
    print(f"Círculo 2: {circ2.obtener_area():.2f}")
    print()

    print("=== Comparación ===")
    mi_cuad = Cuadrado("Negro", 5)
    mi_tri = Triangulo("Blanco", 6, 8, 10)

    area_cuad = mi_cuad.obtener_area()
    area_tri = mi_tri.obtener_area()

    print(f"Área Cuadrado: {area_cuad}")
    print(f"Área Triángulo: {area_tri}")

    if area_cuad > area_tri:
        print(f"Mayor área: cuadrado de color {mi_cuad.get_color()}")
    elif area_tri > area_cuad:
        print(f"Mayor área: triángulo de color {mi_tri.get_color()}")
    else:
        print("Tienen la misma área")