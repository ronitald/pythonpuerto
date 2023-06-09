

class Producto:
    def __init__(self, idProducto, nombre, tipo):
        self.__idProducto = idProducto
        self.__nombre = nombre
        self.__tipo = tipo
    
    def getidProducto(self):
        return self.__idProducto
    
    def __str__(self):
        return self.getNombre()
    
    def getNombre(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def setidProducto(self, producto):
        self.__idProducto = producto

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setTipo(self, tipo):
        self.__tipo = tipo
