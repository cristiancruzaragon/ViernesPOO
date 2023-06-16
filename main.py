from cosas import *


def main():
    pers1 = Persona("Cristian", 20)
    print(pers1)
    print(Persona.descripcion)

    print("---------Herencia Alumno--------")
    al1 = Alumno("Cristian", 20, 1324242, "ICO")
    print(al1)
    print(Alumno.descripcion)
    print("--------------------------------")
    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Terry"
    print(al2)
    al2.dormir()

    print("---------Herencia Profesor---------")
    profe1 = Profesor("Mike", 28 + 3, 35346, "Base de datos")
    print(profe1)
    profe1.dormir()

    print("------Herencia Ayudante Profesor---------")
    ayudante = AyudanteProfesor("Juan", 30, "12345", "Ingeniería", "T123", "Informática", 20)
    print(ayudante)
    ayudante.dormir()
    ayudante.dar_clase("POO")
    ayudante.nombre = "Luis"


main()
