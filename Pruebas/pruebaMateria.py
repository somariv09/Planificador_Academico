from Estructura.Materia import Materia

#Prueba de creación de la materia.
print("PRUEBA 1: Crear una materia")
materia=Materia("mat1", "Matemática I")
print(f"Nombre de la Materia: {materia.nombre} y su código es: {materia.codigo}")

#Prueba de rechazar codigo vacio.
print("\nPRUEBA 2: Excepción de Código Vacio")
try:    
    materia=Materia(" ", "Programación 1")
except ValueError as error:
    print(error)
else:
    print("Error: se acepto codigo vacio")

#Prueba de rechazar cnombre vacio.
print("\nPRUEBA 3: Excepción de Nombre Vacio")
try:    
    materia=Materia("PNR1", "")
except ValueError as error:
    print(error)
else:
    print("Error: se acepto nombre vacio")

#Mostrar como cadena de texto por medio del metodo
print("\nPRUEBA 4: Mostrar codigo y nombre con la función")
materia= Materia("PED", "Programación con Estructuras de Datos")
print(materia.__str__())
