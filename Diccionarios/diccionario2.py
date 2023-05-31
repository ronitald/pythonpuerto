diccionario1 = {}
diccionario2 = {}

def agregar_a_diccionario1(repeticiones, clave, valor, diccionario):
    diccionario.update({clave: valor})
    for i in range(1, repeticiones):
        clave = input('Escriba la clave: ')
        valor = input('Escriba un valor: ')
        diccionario.update({clave: valor})
    return True

def agregar_a_diccionario2(repeticiones, clave, valor, diccionario):
    diccionario.update({clave: valor})
    for i in range(1, repeticiones):
        clave = input('Escriba la clave: ')
        valor = input('Escriba un valor: ')
        diccionario.update({clave: valor})
    return True

def actualizar(diccionario):
    print()
    print('Diccionario:')
    for clave, valor in diccionario.items():
        print(f"{clave} --> {valor}") 

print('Elija el diccionario que desea llenar:')
print('1 o 2')

opcion = int(input('Escriba la opción que desea: '))

if opcion == 1:
    print('Escriba la palabra en español y su respectivo significado en inglés')
    agregar_a_diccionario1(int(input('Cuantas veces quiere llenar el diccionario: ')), input('Escriba la clave: '), input('Escriba el valor: '), diccionario1)
    actualizar(diccionario1)
elif opcion == 2:
    print('Escriba la palabra en inglés y su respectivo significado en español')
    agregar_a_diccionario2(int(input('Cuantas veces quiere llenar el diccionario: ')), input('Escriba la clave: '), input('Escriba el valor: '), diccionario2)
    actualizar(diccionario2)
else:
    print('Opción inválida')
