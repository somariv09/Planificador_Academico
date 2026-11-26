from Estructura.Materia import Materia
from Estructura.Grafo import Grafo
from Estructura.PlanificadorAcademico import PlanificadorAcademico

#Prueba de generar niveles con prerrequsitos.
print("\nPrueba 1: Niveles con Prerrequisitos")

grafo=Grafo()

grafo.AgregarMateria(Materia("Mat1","Matematica I", 5))
grafo.AgregarMateria(Materia("Mat2","Matematica II", 5))
grafo.AgregarMateria(Materia("Prn1","Programación I", 5))
grafo.AgregarMateria(Materia("Esa","Estadistica Aplicada", 5))

grafo.AgregarPrerrequisito("Mat1", "Mat2")
grafo.AgregarPrerrequisito("Mat2", "Prn1")
grafo.AgregarPrerrequisito("Mat2", "Esa")

planificador = PlanificadorAcademico(grafo)
niveles, valido=planificador.generarNiveles()

print("Niveles generados:", niveles)
print("Plan Válido:", valido)
assert valido is True
assert niveles == [["MAT1"], ["MAT2"], ["ESA", "PRN1"]]

#Prueba de generar niveles con materias del mismo grado/niveñ.
print("\nPrueba 2: Materias del mismo nivel")

grafo=Grafo()

grafo.AgregarMateria(Materia("Mat1","Matematica I", 5))
grafo.AgregarMateria(Materia("Esa","Estadistica Aplicada", 5))
grafo.AgregarMateria(Materia("Prn1","Programación I", 5))

planificador = PlanificadorAcademico(grafo)
niveles, valido=planificador.generarNiveles()

print("Niveles generados:", niveles)
print("Plan Válido:", valido)
assert valido is True
assert niveles == [["ESA", "MAT1", "PRN1"]]

#Prueba para detectar dependencias circulares.
print("\nPrueba 3: Dependencia circular")

grafo=Grafo()

grafo.AgregarMateria(Materia("Mat1","Matematica I", 5))
grafo.AgregarMateria(Materia("Mat2","Matematica II", 5))
grafo.AgregarMateria(Materia("Prn1","Programación I", 5))

grafo.AgregarPrerrequisito("Mat1", "Mat2")
grafo.AgregarPrerrequisito("Mat2", "Prn1")
grafo.AgregarPrerrequisito("Prn1", "Mat1")

planificador = PlanificadorAcademico(grafo)
niveles, valido=planificador.generarNiveles()

print("Niveles generados:", niveles)
print("Plan Válido:", valido)
assert valido is False

print("\nPrueba 4: Mostrar Plan de Estudios")

grafo=Grafo()

grafo.AgregarMateria(Materia("Mat1","Matematica I", 5))
grafo.AgregarMateria(Materia("Mat2","Matematica II", 5))
grafo.AgregarMateria(Materia("Prn1","Programación I", 5))
grafo.AgregarMateria(Materia("Esa","Estadistica Aplicada", 5))

grafo.AgregarPrerrequisito("Mat1", "Mat2")
grafo.AgregarPrerrequisito("Mat2", "Prn1")
grafo.AgregarPrerrequisito("Mat2", "Esa")

planificador = PlanificadorAcademico(grafo)
assert planificador.Mostrar() is True


# Validaciones adicionales del algoritmo de planificación.
print("\nPrueba 5: Grafo vacío")
grafoVacio = Grafo()
planificadorVacio = PlanificadorAcademico(grafoVacio)
nivelesVacios, validoVacio = planificadorVacio.generarNiveles()
assert nivelesVacios == []
assert validoVacio is True
assert planificadorVacio.Mostrar() is True
print("Un grafo vacío no genera niveles y se considera válido")

print("\nPrueba 6: Materias independientes y orden estable")
grafoIndependiente = Grafo()
for codigo in ("ZZZ", "AAA", "MMM"):
    assert grafoIndependiente.AgregarMateria(
        Materia(codigo, f"Materia {codigo}", 5)
    )[0] is True
planificadorIndependiente = PlanificadorAcademico(grafoIndependiente)
nivelesIndependientes, validoIndependiente = planificadorIndependiente.generarNiveles()
assert validoIndependiente is True
assert nivelesIndependientes == [["AAA", "MMM", "ZZZ"]]
print("Todas las materias independientes aparecen en el mismo nivel")

print("\nPrueba 7: Dependencia circular de dos materias")
grafoCicloDos = Grafo()
for codigo in ("CIC1", "CIC2"):
    assert grafoCicloDos.AgregarMateria(
        Materia(codigo, f"Materia {codigo}", 5)
    )[0] is True
assert grafoCicloDos.AgregarPrerrequisito("CIC1", "CIC2")[0] is True
assert grafoCicloDos.AgregarPrerrequisito("CIC2", "CIC1")[0] is True
nivelesCicloDos, validoCicloDos = PlanificadorAcademico(grafoCicloDos).generarNiveles()
assert validoCicloDos is False
print("Se detectó correctamente el ciclo de dos materias")

print("\nPrueba 8: Detectar ciclo aunque existan materias independientes")
grafoCicloMixto = Grafo()
for codigo in ("LIBRE", "CIC3", "CIC4", "CIC5"):
    assert grafoCicloMixto.AgregarMateria(
        Materia(codigo, f"Materia {codigo}", 5)
    )[0] is True
assert grafoCicloMixto.AgregarPrerrequisito("CIC3", "CIC4")[0] is True
assert grafoCicloMixto.AgregarPrerrequisito("CIC4", "CIC5")[0] is True
assert grafoCicloMixto.AgregarPrerrequisito("CIC5", "CIC3")[0] is True
nivelesCicloMixto, validoCicloMixto = PlanificadorAcademico(grafoCicloMixto).generarNiveles()
assert validoCicloMixto is False
assert nivelesCicloMixto == [["LIBRE"]]
print("Se detectó el ciclo y se identificó el nivel procesable")

print("\nPrueba 9: Verificar que los niveles respeten los prerrequisitos")
grafoOrden = Grafo()
for codigo in ("A", "B", "C", "D"):
    assert grafoOrden.AgregarMateria(Materia(codigo, f"Materia {codigo}", 5))[0] is True
assert grafoOrden.AgregarPrerrequisito("A", "C")[0] is True
assert grafoOrden.AgregarPrerrequisito("B", "C")[0] is True
assert grafoOrden.AgregarPrerrequisito("C", "D")[0] is True
nivelesOrden, validoOrden = PlanificadorAcademico(grafoOrden).generarNiveles()
assert validoOrden is True
posicion = {codigo: indice for indice, nivel in enumerate(nivelesOrden) for codigo in nivel}
assert posicion["A"] < posicion["C"]
assert posicion["B"] < posicion["C"]
assert posicion["C"] < posicion["D"]
print("Todos los prerrequisitos aparecen antes que sus materias dependientes")

print("\nPrueba 10: Mostrar un plan con dependencia circular")
assert PlanificadorAcademico(grafoCicloDos).Mostrar() is False
print("El método Mostrar informó correctamente que el plan no es válido")
