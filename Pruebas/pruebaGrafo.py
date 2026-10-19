from Estructura.Materia import Materia
from Estructura.Grafo import Grafo

# Crear un grafo y agregar materias.
print("PRUEBA 1: Agregar materias")
grafo=Grafo()

materia1=Materia("MAT1", "Matematica I")
materia2=Materia("MAT2", "Matematica II")
materia3=Materia("PNR1", "Programación I")

print(grafo.AgregarMateria(materia1))
print(grafo.AgregarMateria(materia2))
print(grafo.AgregarMateria(materia3))

#Identificar materias duplicadas por medio de codigos duplicados.
print("PRUEBA 2: Duplicidad de Materias")
try:
    materiaRepetida=Materia("MAT2", "Matematica II")
    grafo.AgregarMateria(materiaRepetida)
except ValueError as error:
    print(error)
else:
    print("Error: se permitió agregar una materia duplicada.")

# Agregar prerrequisitos válidos.
print("\nPRUEBA 3: Agregar prerrequisitos")

# Matemática I es prerrequisito de Matemática II.
prerrequisito1 = grafo.AgregarPrerrequisito("MAT1", "MAT2")
print(prerrequisito1)

# Matemática II es prerrequisito de Programación I.
prerrequisito2 = grafo.AgregarPrerrequisito("MAT2", "PNR1")
print(prerrequisito2)

# Rechazar relaciones con materias inexistentes.
print("\nPRUEBA 4: Rechazar materias no registradas")
try:    
   prerrequisito = grafo.AgregarPrerrequisito("MAT9", "PNR1") 
except ValueError as error:
    print(error)
else:
    print("Error: se acepto materia inexistente")

print("\nPRUEBA 5: Rechazar ser requisito de si misma")
try:    
   prerrequisito = grafo.AgregarPrerrequisito("PNR1", "PNR1") 
except ValueError as error:
    print(error)
else:
    print("Error: se acepto ser requisito de si misma")


print("\nPRUEBA 6: Ingresar la misma relación")
try:    
   prerrequisito = grafo.AgregarPrerrequisito("MAT1", "MAT2")
except ValueError as error:
    print(error)
else:
    print("Error: se acepto una relación ya existente")

print("PRUEBA 7: Listar materias")

listaMaterias = grafo.listarMaterias()

for materia in listaMaterias:
    print(f"{materia.codigo} - {materia.nombre}")


print("\nPRUEBA 8: Obtener códigos")

codigos = grafo.obtenerCodigos()
print(codigos)