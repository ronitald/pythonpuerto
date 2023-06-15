from persona import *

class Instructor(Persona):
    def __init__(self, id, codigo, nombre, direccion, telefono, profesion, especialidad, cargo, salario_basico):
        super().__init__(id, codigo, nombre, direccion, telefono)
        self.__profesion = profesion
        self.__especialidad = especialidad
        self.__cargo = cargo
        self.__salario_basico = salario_basico
        
    def mostrar_informacion(self):
        return f'{self.__profesion}, {self.__especialidad}, {self.__cargo}, {self.__salario_basico}'
