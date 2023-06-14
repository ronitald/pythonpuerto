from individual import *
from compañia import *
from producto import *

clienteIndv = Individual("Ronald", 1, "Puerto", "Gmail.com", 273927)
ProductoUno = Producto(1, "Celular", "Movil")
clienteIndv.agregarProducto(ProductoUno)
print(clienteIndv.getProductos())

# Agregacion

for producto in clienteIndv.getProductos():
    print(producto)

empresaUno = Empresa('CocaCola', 1, 32182)
productoEmpresa = Producto(2, "CocaColaLite", "Bebida")
empresaUno.agregarProducto(productoEmpresa)

for producto in empresaUno.getProductos():
    print(producto)

# Composicion

clienteDos = Individual("Camilo", 1, "Acevedo", "Gmail.com", 4935795)
clienteDos.componerProducto(1, "iPhone", "Celular")
print(clienteDos.getProductos())

empUno = Empresa('CocaCola', 1, 32182)
empUno.componerProducto(2, "CocaColaZero", "Bebida")
print(empUno.getProductos())