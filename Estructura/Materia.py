class Materia:
    def __init__(self, codigo, nombre, uv):
        #Codigo en mayusculas y se eliminan los espacios
        codigo=codigo.strip().upper()
        nombre=nombre.strip()

        #Validaciones que permitan identificar posibles errores de usuario
        #Como por ejemplo ingresar una materia sin codigo
        if not codigo:
            raise ValueError("Ingrese el código de la materia")

        if not nombre:
            raise ValueError("Ingrese el nombre de la materia")

        if isinstance(uv, bool) or not isinstance(uv, int):
            raise ValueError("Las unidades valorativas deben ser un número entero")
        if uv <= 0:
            raise ValueError("Las unidades valorativas deben ser mayores que cero")


        #Ya revisando que los valores sean correctos y existentes los asignamos.
        self.codigo=codigo
        self.nombre=nombre
        self.uv = uv

    def __str__(self):
        return f"{self.codigo}\n {self.nombre} ({self.uv} UV)"
