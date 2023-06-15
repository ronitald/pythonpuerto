from persona import *

class Coordinador(Persona):
    def __init__(self, id, codigo, nombre, direccion, telefono, fecha_ingreso, dir_oficina, nombre_coordinacion):
        super().__init__(id, codigo, nombre, direccion, telefono)
        self._fecha_ingreso = fecha_ingreso
        self._dir_oficina = dir_oficina
        self._nombre_coordinacion = nombre_coordinacion
        
    def getFecha_ingreso(self):
        return self._fecha_ingreso
        
    def setFecha_ingreso(self, fecha_ingreso):
        self._fecha_ingreso = fecha_ingreso
        
    def getDir_oficina(self):
        return self._dir_oficina
        
    def setDir_oficina(self, dir_oficina):
        self._dir_oficina = dir_oficina
        
    def getNombre_coordinacion(self):
        return self._nombre_coordinacion
        
    def mostrar_informacion(self):
        return f'{self._fecha_ingreso}, {self._dir_oficina}, {self._nombre_coordinacion}'