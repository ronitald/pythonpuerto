from individual import *
from compañia import *
from producto import *

clienteIndv = Individual("Ronald", 1, "puerto", ".com", 273927)
ProductoUno = Producto(1, "celular", "movil")
clienteIndv.agregarProducto(ProductoUno)
print(clienteIndv.getProductos())
#Agregacion

for i in clienteIndv.getProductos():
    print(ProductoUno.getNombre())

empresaUno = Empresa('CocaCola', 1, 32182)

productoEmpresa = Producto(2, "CocaColaLite", "Bebida")

empresaUno.agregarProducto(productoEmpresa)

for x in empresaUno.getProductos():
    print(productoEmpresa.getNombre())

#Composicion

clienteDos = Individual("Camilo", "1", "puerto,", "ronald@gmail.om", 4935795)

clienteDos.componerProducto(1, "ihone", "celuco")
print(clienteDos.getProductos())

empUno = Empresa('CocaCola', 1, 32182)

empUno.componerProducto(2, "cuatro", "bebida")
print(empUno.getProductos())