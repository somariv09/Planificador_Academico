from Materia import Materia

class Grafo:
    def __init__(self):
        #Se utiliza un diccionario para guardar codigo y materia. Este sería el nodo del grafo.
        self.materias={}
        #Diccionario que guarda el codigo de la materia que sería el prerrquisito y a la que da acceso. Sería la arista.
        self.prerrequisitos={}

    def AgregarMateria(self, materia:Materia):
        if not isinstance(materia, Materia):
            raise TypeError("Ingrese una materia")
        #Comprobamos que el codigo de la meteria no se repita
        if materia.codigo in self.materias:
            return False, f"Ya existe una materia con el codigo: {materia.codigo}"

        #Los diccionarios usan pares de clave-valor por tanto en el diccionario la clave es el codigo
        #Y con esa podemos acceder al valor que es el nombre de la materia.
        self.materias[materia.codigo]=materia
        self.prerrequisitos[materia.codigo]=[]
        return True, f"Materia {materia.codigo} agregada correctamente"

    def AgregarPrerrequisito(self, codPrerrequisito, codMateria):
        prerrequisito=codPrerrequisito.strip().upper()
        materiaSiguiente=codMateria.strip().upper()

        if prerrequisito not in self.materias or materiaSiguiente not in self.materias:
            return False, f"Se debe registrar primero las materias."

        if prerrequisito==materiaSiguiente:
            return False, f"La materia no puede ser prerrequisito de si misma."

        if materiaSiguiente in self.prerrequisitos[prerrequisito]:
            return False, f"Esta relación de prerrequisito ya fue ingresada."

        #Se crea la arista que va de prerrequisito hacia la materia dependiente.
        self.prerrequisitos[prerrequisito].append(materiaSiguiente)
        return True, f"{prerrequisito} es prerrequisito de {materiaSiguiente}"

    def listarMaterias(self):
        listaMaterias=[]
        codOrdenados= sorted(self.materias)

        for codigo in codOrdenados:
            materia=self.materias[codigo]
            listaMaterias.append(materia)

        return listaMaterias
