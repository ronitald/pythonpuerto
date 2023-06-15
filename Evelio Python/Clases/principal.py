from persona import Persona

persona1 = Persona(1, 11, 'Ronald', 'Cra 77', 312)
persona2 = Persona(2, 12, 'Pedro', 'Trasversal 01', 311)
persona3 = Persona(3, 13, 'Juan', 'Diag 21', 314)
persona4 = Persona(4, 14, 'Cris', 'Calle 100', 310)
persona5 = Persona(5, 15, 'Maikol', 'Calle 116', 300)

print(persona1.mostrar_informacion())
print(persona2.mostrar_informacion())
print(persona3.mostrar_informacion())
print(persona4.mostrar_informacion())
print(persona5.mostrar_informacion())
print()

from instructor import *

from instructor import Instructor

instructor1 = Instructor(1, 11, 'Ronald', 'Cra 77', 312, 'SOFTWARE', 'ADSO', 'Instructor', 5000000 )
instructor2 = Instructor(2, 12, 'Pedro', 'Trasversal 01', 311, 'ADMINISTRADOR', 'Gestion Administrativa', 'Instructor', 6000000)
instructor3 = Instructor(3, 13, 'Juan', 'Diag 21', 314, 'DISEÑO', 'Multimedia', 'Instructor', 4500000)
instructor4 = Instructor(4, 14, 'Cris', 'Calle 100', 310, 'ARQUITECTO', 'Construccion', 'Instructor', 7500000)
instructor5 = Instructor(5, 15, 'Maikol', 'Calle 116', 300, 'EMPRESARIO', 'Emprendimiento', 'Instructor', 4500000)

print(instructor1.mostrar_informacion())
print(instructor2.mostrar_informacion())
print(instructor3.mostrar_informacion())
print(instructor4.mostrar_informacion())
print(instructor5.mostrar_informacion())
print()

from coordinador import Coordinador

coordinador1 = Coordinador(1, 11, 'Ronald', 'Cra 77', 312, '06/11/2020', 'Oficina 10', 'Coordinador Academico')
coordinador2 = Coordinador(2, 12, 'Pedro', 'Trasversal 01', 311, '06/11/2020', 'Oficina 11', 'Coordinador Academico')
coordinador3 = Coordinador(3, 13, 'Juan', 'Diag 21', 314, '06/11/2020', 'Oficina 12', 'Coordinador Academico')
coordinador4 = Coordinador(4, 14, 'Cris', 'Calle 100', 310, '06/11/2020', 'Oficina 13', 'Coordinador Academico')
coordinador5 = Coordinador(5, 15, 'Maikol', 'Calle 116', 300, '06/11/2020', 'Oficina 14', 'Coordinador Academico')

print(coordinador1.mostrar_informacion())
print(coordinador2.mostrar_informacion())
print(coordinador3.mostrar_informacion())
print(coordinador4.mostrar_informacion())
print(coordinador5.mostrar_informacion())
print()