# Planificador Académico
Este es un proyecto en python que permite ingresar materias y los prerrequisitos de esta  para generar un planificador acedemico por medio de grafos y el algoritmo de kahn.

# tecnologías.
Python 3.14.7
Git
GitHub

# Estructura
-\Estructura: Es donde se encuentra el codigo fuente que incluye la clase de materias, Grafo, PlanificadorAcademico y el Main.
-\Pruebas: Las pruebas con datos precargados para corroborar el funcionamiento del sistema.

## Funcionamiento del sistema

El sistema utiliza un grafo para representar las materias y sus relaciones de prerrequisito. A partir de estas relaciones, el planificador aplica el algoritmo de Kahn para determinar un orden válido de las materias y agruparlas por niveles académicos.

### Estructuras de datos utilizadas

- **Grafo:** almacena las materias y las relaciones de dependencia entre ellas.
- **Cola:** permite procesar las materias que ya cumplen con sus prerrequisitos, siguiendo el orden FIFO.
- **Listas:** permiten almacenar y organizar las materias correspondientes a cada nivel académico.
- **Diccionarios:** facilitan la consulta de las materias y sus relaciones mediante sus códigos.

### Algoritmo de Kahn

El algoritmo identifica inicialmente las materias que no tienen prerrequisitos pendientes. Estas se procesan y se agrupan en un nivel. Posteriormente, se actualizan las dependencias de las materias relacionadas para identificar cuáles pueden incorporarse al siguiente nivel.

Este procedimiento continúa hasta procesar todas las materias o detectar que existen dependencias circulares que impiden generar un plan válido.

### Validaciones

El sistema contempla validaciones relacionadas con el registro de materias y sus prerrequisitos. También verifica si es posible procesar todas las materias para determinar si las dependencias permiten generar un plan académico válido.

### Alcance actual

El proyecto se enfoca en generar un plan académico a partir de las materias registradas y sus prerrequisitos. Las funcionalidades disponibles dependen de la implementación actual del código fuente.
