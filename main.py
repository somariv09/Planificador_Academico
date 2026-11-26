from Estructura.Materia import Materia
from Estructura.Grafo import Grafo
from Estructura.PlanificadorAcademico import PlanificadorAcademico


def mostrar_menu():
    print("\n========== PLANIFICADOR ACADÉMICO ==========")
    print("1. Registrar materia")
    print("2. Registrar prerrequisito")
    print("3. Listar materias")
    print("4. Mostrar plan académico por niveles")
    print("5. Salir")


def mostrar_resumen_uv(grafo):
    print(f"Unidades valorativas acumuladas: {grafo.obtenerUVTotal()}/{grafo.LIMITE_UV} UV")


def solicitar_uv():
    while True:
        entrada = input("Unidades valorativas (UV, número entero): ").strip()

        try:
            uv = int(entrada)
        except ValueError:
            print("Entrada no válida. Ingrese las UV como un número entero, por ejemplo: 3.")
            continue

        if uv <= 0:
            print("Las unidades valorativas deben ser mayores que cero. Inténtelo nuevamente.")
            continue

        return uv


def registrar_materia(grafo):
    print("\n--- REGISTRO DE MATERIA ---")
    codigo = input("Código de la materia: ").strip()
    nombre = input("Nombre de la materia: ").strip()

    if not codigo:
        print("No se registró la materia: debe ingresar un código.")
        return

    if not nombre:
        print("No se registró la materia: debe ingresar un nombre.")
        return

    uv = solicitar_uv()

    try:
        materia = Materia(codigo, nombre, uv)
    except (ValueError, AttributeError) as error:
        print(f"No se pudo registrar la materia: {error}")
        return

    correcto, mensaje = grafo.AgregarMateria(materia)
    print(mensaje)
    mostrar_resumen_uv(grafo)


def registrar_prerrequisito(grafo):
    print("\n--- REGISTRO DE PRERREQUISITO ---")
    codigo_prerrequisito = input("Código de la materia prerrequisito: ").strip()
    codigo_materia = input("Código de la materia dependiente: ").strip()

    print("\nCONFIRMACIÓN DE LA RELACIÓN")
    print(f"{codigo_prerrequisito.upper()} será prerrequisito de {codigo_materia.upper()}.")

    while True:
        confirmacion = input("¿Desea guardar esta relación? (S/N): ").strip().upper()

        if confirmacion == "S":
            correcto, mensaje = grafo.AgregarPrerrequisito(
                codigo_prerrequisito, codigo_materia
            )
            print(mensaje)
            if correcto:
                print("La relación se ha guardado correctamente.")
            return

        if confirmacion == "N":
            print("Operación cancelada. No se realizaron cambios.")
            return

        print("Opción no válida. Escriba S para confirmar o N para cancelar.")


def listar_materias(grafo):
    print("\n--- MATERIAS REGISTRADAS ---")
    materias = grafo.listarMaterias()

    if not materias:
        print("No hay materias registradas.")
        return

    for materia in materias:
        print(f"{materia.codigo} - {materia.nombre} - {materia.uv} UV")

    mostrar_resumen_uv(grafo)


def mostrar_plan(grafo):
    print("\n--- PLAN ACADÉMICO ---")
    PlanificadorAcademico(grafo).Mostrar()
    mostrar_resumen_uv(grafo)


def main():
    grafo = Grafo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_materia(grafo)
        elif opcion == "2":
            registrar_prerrequisito(grafo)
        elif opcion == "3":
            listar_materias(grafo)
        elif opcion == "4":
            mostrar_plan(grafo)
        elif opcion == "5":
            print("\nSaliendo del Planificador Académico. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Seleccione una opción del 1 al 5.")


if __name__ == "__main__":
    main()
