
def usar_d1(palabra, diccionario):
    if palabra in diccionario:
        print(f'{palabra} en inglés es: {diccionario[palabra]}')
    else:
        print(f'No se encontró la palabra {palabra} en el diccionario.')

def usar_d2(word, diccionario):
    if word in diccionario:
        print(f'{word} en español es: {diccionario[word]}')
    else:
        print(f'No se encontró la palabra {word} en el diccionario.')

def menu_agregar(diccionario):
    print('Elija el diccionario que desea llenar:')
    print('1: Español-Inglés')
    print('2: Inglés-Español')

    opcion = int(input('Seleccione la opción que desea: '))

    if opcion == 1:
        print('Escriba la palabra en español y su respectivo significado en inglés')
        agregar_d1(int(input('¿Cuántas palabras desea agregar al diccionario?: ')), diccionario)
        mostrar_diccionario(diccionario)
    elif opcion == 2:
        print('Escriba la palabra en inglés y su respectivo significado en español')
        agregar_d2(int(input('¿Cuántas palabras desea agregar al diccionario?: ')), diccionario)
        mostrar_diccionario(diccionario)
    else:
        print('Opción no válida.')

def menu_principal(dic1, dic2):
    print('Elija el diccionario que desea usar:')
    print('1: Español-Inglés')
    print('2: Inglés-Español')
    print('3: Consultar diccionario 1')
    print('4: Consultar diccionario 2')

    opcion = int(input('Seleccione la opción que desea: '))

    if opcion == 1:
        print('Diccionario Español-Inglés:')
        palabra = input('Ingrese una palabra en español: ')
        usar_d1(palabra, dic1)
    elif opcion == 2:
        print('Diccionario Inglés-Español:')
        word = input('Ingrese una palabra en inglés: ')
        usar_d2(word, dic2)
    elif opcion == 3:
        mostrar_diccionario(dic1)
    elif opcion == 4:
        mostrar_diccionario(dic2)
    else:
        print('Opción no válida.')

dic1 = {}
dic2 = {}
menu_principal(dic1, dic2)