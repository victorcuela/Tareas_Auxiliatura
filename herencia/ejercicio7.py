import copy
# Clase base
class Documento:
    def __init__(self, titulo, autores, editorial, anio):
        self.titulo = titulo
        self.autores = autores
        self.editorial = editorial
        self.anio = anio
    def __str__(self):
        return f"{self.titulo} - {self.autores} ({self.anio})"
# Libro
class Libro(Documento):
    def __init__(self, titulo, autores, editorial, anio):
        super().__init__(titulo, autores, editorial, anio)
# Revista
class Revista(Documento):
    def __init__(self, titulo, autores, editorial, anio, volumen, numero, mes):
        super().__init__(titulo, autores, editorial, anio)
        self.volumen = volumen
        self.numero = numero
        self.mes = mes
# Revista de investigación
class RevistaInvestigacion(Revista):
    def __init__(self, titulo, autores, editorial, anio, volumen, numero, mes, campo_inv):
        super().__init__(titulo, autores, editorial, anio, volumen, numero, mes)
        self.campo_inv = campo_inv
# Documento en CD
class DocumentoCD(Documento):
    def __init__(self, titulo, autores, editorial, anio, formato_cd, tipo_licencia):
        super().__init__(titulo, autores, editorial, anio)
        self.formato_cd = formato_cd
        self.tipo_licencia = tipo_licencia
# Biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista = []

    def agregar(self, doc):
        self.lista.append(doc)

    def contar_revistas(self):
        cont = 0
        for d in self.lista:
            if isinstance(d, Revista):
                cont += 1
        return cont

    def contar_total(self):
        return len(self.lista)

    def mostrar(self):
        print(f"\n--- {self.nombre} ---")
        for d in self.lista:
            print(f"- {d}")

    def copia(self, otra):
        otra.lista = copy.deepcopy(self.lista)
# ------ PRINCIPAL -------
if __name__ == "__main__":
    # b) Crear 2 bibliotecas
    b1 = Biblioteca("Biblioteca 1")
    b2 = Biblioteca("Biblioteca 2")
    # Cosas para la biblioteca 1
    b1.agregar(Libro("El Quijote", "Cervantes", "Editorial A", 1605))
    b1.agregar(Libro("Cien años de soledad", "García Márquez", "Editorial B", 1967))
    b1.agregar(RevistaInvestigacion("Matemáticas hoy", "Varios", "Editorial C", 2024, 5, 10, "Enero", "Matemáticas"))
    b1.agregar(DocumentoCD("Curso de Java", "Profesor ", "Editorial D", 2023, "DVD", "Estudiantil"))
    # Cosas para la biblioteca 2
    b2.agregar(Libro("Harry Potter", "J.K. Rowling", "Editorial E", 1997))
    b2.agregar(Revista("Naturaleza", "Varios", "Editorial F", 2024, 12, 3, "Marzo"))
    b2.agregar(RevistaInvestigacion("Física moderna", "Equipo", "Editorial G", 2023, 8, 2, "Febrero", "Física"))
    b2.agregar(Revista("Tecnología", "Redacción", "Editorial H", 2024, 7, 6, "Junio"))

    print("=== ESTADO INICIAL ===")
    b1.mostrar()
    b2.mostrar()

    print("\n=== COMPARACIÓN ===")
    r1 = b1.contar_revistas()
    r2 = b2.contar_revistas()
    t1 = b1.contar_total()
    t2 = b2.contar_total()
    if r1 > r2:
        print(f"Más revistas: {b1.nombre} ({r1} contra {r2})")
    elif r2 > r1:
        print(f"Más revistas: {b2.nombre} ({r2} contra {r1})")
    else:
        print(f"Mismas revistas: {r1} cada una")

    if t1 > t2:
        print(f"Más documentos: {b1.nombre} ({t1} contra {t2})")
    elif t2 > t1:
        print(f"Más documentos: {b2.nombre} ({t2} contra {t1})")
    else:
        print(f"Mismos documentos: {t1} cada una")
    # c) Trasladar: revistas a b1, libros a b2
    revistas_b2 = []
    libros_b1 = []
    for d in b2.lista:
        if isinstance(d, Revista):
            revistas_b2.append(d)
    for d in b1.lista:
        if isinstance(d, Libro):
            libros_b1.append(d) 
    # Quitar los que se van
    b1.lista = [d for d in b1.lista if not isinstance(d, Libro)]
    b2.lista = [d for d in b2.lista if not isinstance(d, Revista)]

    # Agregar en el otro
    b1.lista.extend(revistas_b2)
    b2.lista.extend(libros_b1)
    print("\n=== DESPUÉS DE TRASLADAR ===")
    b1.mostrar()
    b2.mostrar()
    # d) Copia de seguridad
    respaldo1 = Biblioteca("Respaldo 1")
    respaldo2 = Biblioteca("Respaldo 2")
    b1.copia(respaldo1)
    b2.copia(respaldo2)

    print("\n=== COPIAS DE SEGURIDAD ===")
    respaldo1.mostrar()
    respaldo2.mostrar()