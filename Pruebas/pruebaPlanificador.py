from Estructura.Materia import Materia
from Estructura.Grafo import Grafo
from Estructura.PlanificadorAcademico import PlanificadorAcademico

#Prueba de generar niveles con prerrequsitos.
print("\nPrueba 1: Niveles con Prerrequisitos")

grafo=Grafo()

grafo.AgregarMateria(Materia("Mat1","Matematica I"))
grafo.AgregarMateria(Materia("Mat2","Matematica II"))
grafo.AgregarMateria(Materia("Prn1","Programación I"))
grafo.AgregarMateria(Materia("Esa","Estadistica Aplicada"))

grafo.AgregarPrerrequisito("Mat1", "Mat2")
grafo.AgregarPrerrequisito("Mat2", "Prn1")
grafo.AgregarPrerrequisito("Mat2", "Esa")

planificador = PlanificadorAcademico(grafo)
niveles, valido=planificador.generarNiveles()

print("Niveles generados:", niveles)
print("Plan Válido:", valido)

#Prueba de generar niveles con materias del mismo grado/niveñ.
print("\nPrueba 2: Materias del mismo nivel")

grafo=Grafo()

grafo.AgregarMateria(Materia("Mat1","Matematica I"))
grafo.AgregarMateria(Materia("Esa","Estadistica Aplicada"))
grafo.AgregarMateria(Materia("Prn1","Programación I"))

planificador = PlanificadorAcademico(grafo)
niveles, valido=planificador.generarNiveles()

print("Niveles generados:", niveles)
print("Plan Válido:", valido)

#Prueba para detectar dependencias circulares.
print("\nPrueba 3: Dependencia circular")

grafo=Grafo()

grafo.AgregarMateria(Materia("Mat1","Matematica I"))
grafo.AgregarMateria(Materia("Mat2","Matematica II"))
grafo.AgregarMateria(Materia("Prn1","Programación I"))

grafo.AgregarPrerrequisito("Mat1", "Mat2")
grafo.AgregarPrerrequisito("Mat2", "Prn1")
grafo.AgregarPrerrequisito("Prn1", "Mat1")

planificador = PlanificadorAcademico(grafo)
niveles, valido=planificador.generarNiveles()

print("Niveles generados:", niveles)
print("Plan Válido:", valido)

print("\nPrueba 4: Mostrar Plan de Estudios")

grafo=Grafo()

grafo.AgregarMateria(Materia("Mat1","Matematica I"))
grafo.AgregarMateria(Materia("Mat2","Matematica II"))
grafo.AgregarMateria(Materia("Prn1","Programación I"))
grafo.AgregarMateria(Materia("Esa","Estadistica Aplicada"))

grafo.AgregarPrerrequisito("Mat1", "Mat2")
grafo.AgregarPrerrequisito("Mat2", "Prn1")
grafo.AgregarPrerrequisito("Mat2", "Esa")

planificador = PlanificadorAcademico(grafo)
planificador.Mostrar()
