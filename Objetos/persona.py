class Persona:
    def __init__(self, nombre, documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__cursos = []

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDocumento(self):
        return self.__documento

    def setDocumento(self, documento):
        self.__documento = documento

    def agregarCurso(self, curso):
        self.__cursos.append(curso)

    def getCursos(self):
        return self.__cursos



p = Persona('Ana', 123)
print(p.getNombre()) 

q = Persona('Pedro', 321)
print(q.getNombre()) 

print(p.getDocumento())
print(q.getDocumento())

p.agregarCurso('Matematicas')
print(p.getCursos())

q.agregarCurso('Ingles')
print(q.getCursos())
