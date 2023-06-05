class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario
    
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, cargo):
        self.__cargo = cargo
    
    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__cargo = salario

persona1 = Empleado()


#1000*(13,12/100)