from Estructura.Materia import Materia

#Prueba de creación de la materia.
print("PRUEBA 1: Crear una materia")
materia=Materia("mat1", "Matemática I", 5)
print(f"Nombre de la Materia: {materia.nombre} y su código es: {materia.codigo}")
assert materia.codigo == "MAT1"
assert materia.nombre == "Matemática I"
assert materia.uv == 5

#Prueba de rechazar codigo vacio.
print("\nPRUEBA 2: Excepción de Código Vacio")
try:    
    materia=Materia(" ", "Programación 1", 5)
except ValueError as error:
    print(error)
else:
    raise AssertionError("Se aceptó un código vacío")

#Prueba de rechazar nombre vacio.
print("\nPRUEBA 3: Excepción de Nombre Vacio")
try:    
    materia=Materia("PNR1", "", 5)
except ValueError as error:
    print(error)
else:
    raise AssertionError("Se aceptó un nombre vacío")

#Mostrar como cadena de texto por medio del metodo
print("\nPRUEBA 4: Mostrar codigo y nombre con la función")
materia= Materia("PED", "Programación con Estructuras de Datos", 4)
print(materia.__str__())
assert str(materia) == "PED\n Programación con Estructuras de Datos (4 UV)"




# Prueba de validación de unidades valorativas.
print("\nPRUEBA 5: Validación de Unidades Valorativas")
for valor_uv in (0, -1):
    try:
        Materia("UV1", "Materia de prueba", valor_uv)
    except ValueError as error:
        print(error)
    else:
        raise AssertionError("Se aceptaron unidades valorativas no positivas")
try:
    Materia("UV2", "Materia de prueba", "cinco")
except ValueError as error:
    print(error)
else:
    raise AssertionError("Se aceptaron unidades valorativas no enteras")


# Validaciones adicionales de formato y normalización.
print("\nPRUEBA 6: Normalización de código y espacios")
materiaNormalizada = Materia("  ped2026  ", "  Estructuras de Datos  ", 5)
assert materiaNormalizada.codigo == "PED2026"
assert materiaNormalizada.nombre == "Estructuras de Datos"
print("Código y nombre normalizados correctamente")

print("\nPRUEBA 7: Rechazar UV decimales")
try:
    Materia("UV3", "Materia decimal", 3.5)
except ValueError as error:
    print(error)
else:
    raise AssertionError("Se aceptaron unidades valorativas decimales")

print("\nPRUEBA 8: Rechazar valores booleanos como UV")
try:
    Materia("UV4", "Materia con UV booleanas", True)
except ValueError as error:
    print(error)
else:
    raise AssertionError("Se aceptó True como cantidad de UV")

print("\nPRUEBA 9: Rechazar UV de tipo lista")
try:
    Materia("UV5", "Materia con UV inválidas", [5])
except ValueError as error:
    print(error)
else:
    raise AssertionError("Se aceptó una lista como cantidad de UV")

print("\nPRUEBA 10: Verificar que el objeto conserve sus datos")
assert materiaNormalizada.codigo == "PED2026"
assert materiaNormalizada.nombre == "Estructuras de Datos"
assert materiaNormalizada.uv == 5
print("Los datos de la materia se conservaron correctamente")
