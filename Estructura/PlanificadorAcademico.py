from collections import deque
from Grafo import Grafo

class PlanificadorAcademico:
    def __init__(self, grafo:Grafo):
        self.grafo=grafo

    def generarNiveles(self):
        #Se ontienen el listado de codigos de las materias ingresadas.
        codigos=self.grafo.obtenerCodigos()

        #Se asigna grado 0 de entrada para inicializar
        gradoEntrada={x:0 for x in codigos}

        #Se recorre la lista de codigos
        for x in codigos:
            #Se recorre los prerrequisitos de un codigo en especifico
            for y in self.grafo.prerrequisitos[x]:
                #Se aumenta el grado de entrada
                gradoEntrada[y]+=1

        codigosGradoCero=[]

        #Si el codigo es de grado cero se añade a la lista
        for x in codigos:
            if(gradoEntrada[x]==0):
                codigosGradoCero.append[x]

        codOrdenados=sorted(codigosGradoCero)
        #Se asigna la lista con codigos grado cero a una cola para empezar a procesar
        cola=deque(codOrdenados)

        niveles=[]
        procesado=0

        while cola:
            #Se obtiene la longitud de la cola, ejemplo si hay una codigo de grado cero entonces la longitud es 1
            materiasCola=len(cola)
            nivelActual=[]

            for __ in range(materiasCola):
                #Se elimina el codigo de la cola
                codigo=cola.popleft()
                #Y se añade a la lista
                nivelActual.append(codigo)
                procesado+=1    

                #Se recorren los prerrequisitos pertenecientes al codigo
                for prerrequisito in self.grafo.prerrequisitos[codigo]:
                    #Se les reduce un grado
                    gradoEntrada[prerrequisito]-=1

                    #Cuando el grado sea igual a cero se añade a la cola
                    if gradoEntrada[prerrequisito]==0:
                        cola.append(prerrequisito)
            nivelActual.sort()
            #Se guarda nivelActual en niveles, la cual es una lista de listas.
            niveles.append(nivelActual)
        #Condición que muestra un error con las materias procesadas por relaciones circulares o donde es imposible cumplir los prerrequisitos.
        if procesado != len(codigos):
            return niveles, False

        return niveles, True

    def Mostrar(self):
        niveles, valido=self.generarNiveles()

        if not valido:
            print("\nNo es posible generar el plan de estudios.\nSe detecta una dependencia circular")
            return False
        if not niveles:
            print("\nNo hay materias para generar un plan de estudios")
            return True
        
        print("\nPLAN DE ESTUDIOS ORGANIZADO POR NIVELES")
        #enumerate permite obtener el los codigos de la lista niveles y el numero de vuelta iniciando en 1
        for num, nivel in enumerate(niveles, start=1):
            print(f"Nivel {num}:")
            #Se recorre la lista de codigos de ese nivel
            for x in nivel:
                #Se obtiene el objeto Materia (codigo y nombre)
                materia = self.grafo.materias[x]
                #Se imprime
                print(f"  - {materia}")
        return True
