class DashboardError(Exception):
    """Clase base para otros errores en este proyecto"""
    pass

class APIConnectionError(DashboardError):
    """Se lanza cuando no podemos conectar con el proveedor de datos"""
    def __init__(self, mensaje="Error: No se pudo conectar con la API externa."):
        self.message = mensaje
        super().__init__(self.message)

class DatabaseIntegrityError(DashboardError):
    """Se lanza cuando hay un problema guardando los datos en SQLite"""
    pass