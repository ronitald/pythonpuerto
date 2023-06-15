class Persona:
    def __init__(self, id, codigo, nombre, direccion, telefono):
        self.id = id
        self.nombre = nombre
        self.codigo = codigo
        self.direccion = direccion
        self.telefono = telefono
    
    def mostrar_informacion(self):
        return f'{self.id}, {self.codigo}, {self.nombre}, {self.direccion}, {self.telefono}'

