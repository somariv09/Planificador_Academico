from Estructura.Materia import Materia
from Estructura.Grafo import Grafo

# Crear un grafo y agregar materias.
print("PRUEBA 1: Agregar materias")
grafo=Grafo()

materia1=Materia("MAT1", "Matematica I", 60)
materia2=Materia("MAT2", "Matematica II", 50)
materia3=Materia("PNR1", "Programación I", 40)

print(grafo.AgregarMateria(materia1))
print(grafo.AgregarMateria(materia2))
print(grafo.AgregarMateria(materia3))
assert len(grafo.materias) == 3
assert grafo.obtenerCodigos() == ["MAT1", "MAT2", "PNR1"]

#Identificar materias duplicadas por medio de codigos duplicados.
print("PRUEBA 2: Duplicidad de Materias")
materiaRepetida=Materia("MAT2", "Matematica II", 50)
resultadoDuplicado = grafo.AgregarMateria(materiaRepetida)
print(resultadoDuplicado)
assert resultadoDuplicado[0] is False
assert len(grafo.materias) == 3

# Agregar prerrequisitos válidos.
print("\nPRUEBA 3: Agregar prerrequisitos")

# Matemática I es prerrequisito de Matemática II.
prerrequisito1 = grafo.AgregarPrerrequisito("MAT1", "MAT2")
print(prerrequisito1)

# Matemática II es prerrequisito de Programación I.
prerrequisito2 = grafo.AgregarPrerrequisito("MAT2", "PNR1")
print(prerrequisito2)
assert prerrequisito1[0] is True
assert prerrequisito2[0] is True

# Rechazar relaciones con materias inexistentes.
print("\nPRUEBA 4: Rechazar materias no registradas")
prerrequisito = grafo.AgregarPrerrequisito("MAT9", "PNR1")
print(prerrequisito)
assert prerrequisito[0] is False

print("\nPRUEBA 5: Rechazar ser requisito de si misma")
prerrequisito = grafo.AgregarPrerrequisito("PNR1", "PNR1")
print(prerrequisito)
assert prerrequisito[0] is False

print("\nPRUEBA 6: Ingresar la misma relación")
prerrequisito = grafo.AgregarPrerrequisito("MAT1", "MAT2")
print(prerrequisito)
assert prerrequisito[0] is False
assert grafo.prerrequisitos["MAT1"] == ["MAT2"]

print("PRUEBA 7: Listar materias")

listaMaterias = grafo.listarMaterias()

for materia in listaMaterias:
    print(f"{materia.codigo} - {materia.nombre}")


print("\nPRUEBA 8: Obtener códigos")

codigos = grafo.obtenerCodigos()
print(codigos)
assert codigos == ["MAT1", "MAT2", "PNR1"]
assert [m.codigo for m in listaMaterias] == ["MAT1", "MAT2", "PNR1"]
# Validar que no se supere el límite total de 170 UV.
print("\nPRUEBA 9: Límite de Unidades Valorativas")
assert grafo.obtenerUVTotal() == 150
materiaExcedeUV = Materia("UVEX", "Materia que excede el límite", 21)
resultadoUV = grafo.AgregarMateria(materiaExcedeUV)
print(resultadoUV)
assert resultadoUV[0] is False
assert grafo.obtenerUVTotal() == 150

# Una materia que deja el total exactamente en 170 UV sí debe aceptarse.
materiaLimiteUV = Materia("UVOK", "Materia dentro del límite", 20)
resultadoUV = grafo.AgregarMateria(materiaLimiteUV)
print(resultadoUV)
assert resultadoUV[0] is True
assert grafo.obtenerUVTotal() == 170


# Validaciones adicionales del registro y del acumulado de UV.
print("\nPRUEBA 10: Rechazar código duplicado sin alterar el total")
totalAntesDuplicado = grafo.obtenerUVTotal()
duplicadaConOtroNombre = Materia("MAT1", "Nombre diferente", 10)
resultado = grafo.AgregarMateria(duplicadaConOtroNombre)
print(resultado)
assert resultado[0] is False
assert grafo.obtenerUVTotal() == totalAntesDuplicado
assert len(grafo.materias) == 4

print("\nPRUEBA 11: Rechazar materia que supera el límite por una UV")
grafoLimite = Grafo()
assert grafoLimite.AgregarMateria(Materia("BASE", "Materia base", 169))[0] is True
resultado = grafoLimite.AgregarMateria(Materia("EXTRA", "Una UV adicional", 2))
print(resultado)
assert resultado[0] is False
assert grafoLimite.obtenerUVTotal() == 169
assert "171" in resultado[1]

print("\nPRUEBA 12: Aceptar materia que completa exactamente el límite")
resultado = grafoLimite.AgregarMateria(Materia("FINAL", "Completa límite", 1))
print(resultado)
assert resultado[0] is True
assert grafoLimite.obtenerUVTotal() == 170

print("\nPRUEBA 13: Rechazar códigos vacíos en prerrequisitos")
assert grafo.AgregarPrerrequisito("", "MAT1")[0] is False
assert grafo.AgregarPrerrequisito("MAT1", "")[0] is False
assert grafo.AgregarPrerrequisito("   ", "MAT1")[0] is False
print("Se rechazaron códigos vacíos o con espacios")

print("\nPRUEBA 14: Aceptar prerrequisito con espacios y minúsculas")
grafoFormato = Grafo()
assert grafoFormato.AgregarMateria(Materia("CURSO1", "Curso 1", 5))[0] is True
assert grafoFormato.AgregarMateria(Materia("CURSO2", "Curso 2", 5))[0] is True
resultado = grafoFormato.AgregarPrerrequisito(" curso1 ", " curso2 ")
print(resultado)
assert resultado[0] is True
assert grafoFormato.prerrequisitos["CURSO1"] == ["CURSO2"]

print("\nPRUEBA 15: Comprobar listado ordenado y total de UV")
codigosOrdenados = [materia.codigo for materia in grafo.listarMaterias()]
assert codigosOrdenados == sorted(codigosOrdenados)
assert grafo.obtenerUVTotal() == sum(materia.uv for materia in grafo.materias.values())
print("Listado ordenado y acumulado de UV correctos")
