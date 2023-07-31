from producto import Producto

class Cliente:
    def __init__(self, nombre, id_cliente):
        self.__nombre = nombre
        self.__idCliente = id_cliente
        self.__productos = []
        self.__precio = 0

    def getId(self):
        return self.__idCliente
    
    def getPrecio(self):
        return self.__precio
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setPrecio(self, precio):
        self.__precio = precio

    def agregarProducto(self, producto):
        self.__productos.append(producto)
        self.__precio += producto.getPrecio()

    def __str__(self):
        return self.__productos

    def getProductos(self):
        return self.__productos
    
    def componerProducto(self, id, nombre, precio):
        productoUno = Producto(id, nombre, precio)
        self.agregarProducto(productoUno)
