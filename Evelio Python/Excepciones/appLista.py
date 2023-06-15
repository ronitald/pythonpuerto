from ActividadLista import *

print('1- Lista lenguajes de programación.')
print('2- Lista de regionales.')
print('3- Lista de números pares.')
print('4- Lista de múltiplos de cuatro.')
print('5- Lista de nombres de aprendices.')
print('6- Lista solo de letras.')
print()

while True:
    opcion = int(input('Elija la lista que desea usar: '))
    print()
    if opcion == 1:
        lenguajes()
    elif opcion == 2:
        regionales()
    elif opcion == 3:
        numPares()
    elif opcion == 4:
        multiplosCuatro()
    elif opcion == 5:
        nombreAprendiz()
    elif opcion == 6:
        letras()
    else:
        print('Error: Ingrese una opcion valida.')