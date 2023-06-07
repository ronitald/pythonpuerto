class Empleado:
    prom = 0
    sumaSalarios = 0

    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario
        Empleado.prom += 1
        Empleado.sumaSalarios += self.__salario

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getCargo(self):
        return self.__cargo

    def setCargo(self, cargo):
        self.__cargo = cargo

    def salarioHora(self, horasTrabajadas):
        salario_hora = self.__salario / horasTrabajadas
        return salario_hora

    def incrementoSalario(self):
        if self.__salario > 1160000:
            ipc = self.__salario * 13.12 / 100
            incrementoSalario = self.__salario + ipc
            self.__salario = incrementoSalario
            return ipc
        else:
            ipc = self.__salario * 16.12 / 100
            incremento = self.__salario + ipc
            self.__salario = incremento
            return ipc

    def horasExtras(self, horas):
        while horas > 10:
            horas = int(input('El numero de horas extras no puede ser mayor a 10. Ingrese las horas nuevamente: '))
        if horas <= 0:
            return 'No se ingresaron horas extra. '
        else:
            suma = 4833 * horas
            self.__salario += suma
            return 'Las horas extra son correctas. '

    def getSuma(self):
        return Empleado.sumaSalarios

    def promedioSalarios(self):
        promSalarios = Empleado.sumaSalarios / Empleado.prom
        return promSalarios

    def getDatos(self):
        return f'{self.__nombre}, {self.__cargo}, {self.__salario}'

print()
p = Empleado('Juan', 'Conductor', 1500000)
print(p.getNombre())
print(p.getCargo())
horas_trab = int(input('Ingrese horas trabajadas: '))
salario_hora = p.salarioHora(horas_trab)
print(f'El empleado {p.getNombre()} gana {round(salario_hora, 2)} por hora')
print(f'El incremento es de: {round(p.incrementoSalario(), 2)}')
print(p.horasExtras(horas_trab))
print(p.getDatos())

print()
q = Empleado('Laura', 'Psicologa', 2500000)
print(q.getNombre())
print(q.getCargo())
horas_trab = int(input('Ingrese horas trabajadas: '))
salario_hora = q.salarioHora(horas_trab)
print(f'El empleado {q.getNombre()} gana {round(salario_hora, 2)} por hora')
print(f'El incremento es de: {round(q.incrementoSalario(), 2)}')
print(q.horasExtras(horas_trab))
print(f'El promedio de los salarios es de: {round(q.promedioSalarios(), 2)}')
print(q.getDatos())

print()
x = Empleado('Pedro', 'Mensajero', 1000000)
print(x.getNombre())
print(x.getCargo())
horas_trab = int(input('Ingrese horas trabajadas: '))
salario_hora = x.salarioHora(horas_trab)
print(f'El empleado {x.getNombre()} gana {salario_hora:.2f} por hora')
print(f'El incremento es de: {round(x.incrementoSalario(), 2)}')
print(q.horasExtras(horas_trab))
print(f'El promedio de los salarios es de: {round(x.promedioSalarios(), 2)}')
print(x.getDatos())