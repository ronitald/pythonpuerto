Lista_lenguajes = []
Lista_regionales = []
Lista_pares = []
Lista_multiplos4 = []
Lista_2693630 = []
Lista_solo_letras = []

def agregar_una_vez(lista, elemento):
    try:
        if elemento in lista:
            raise ValueError('No se puede agregar un elemento duplicado')
        else:
            lista.append(elemento)
            return lista
    except ValueError as ve:
        print(f'Error: {ve}')

while True:
    entrada = input('Ingrese el lenguaje de programación para agregar a la lista: \n(0 para finalizar): ')
    try:
        num = int(entrada)
        if num == 0:
            break
        else:
            agregar_una_vez(Lista_lenguajes, num)
    except ValueError:
        agregar_una_vez(Lista_lenguajes, entrada)
print(f'La lista  de lenguajes es: {Lista_lenguajes}')
print()


while True:
    entrada = input('Ingrese la regional para agregar a la lista: \n(0 para finalizar): ')
    try:
        num = int(entrada)
        if num == 0:
            break
        else:
            agregar_una_vez(Lista_regionales, num)
    except ValueError:
        agregar_una_vez(Lista_regionales, entrada)
print(f'La lista de las regionales es: {Lista_regionales} ')
print()

while True:
    entrada = input('Ingrese números pares para agregar a la lista: \n(0 para finalizar): ')
    try:
        num = int(entrada)
        if num == 0:
            break
        if num % 2 != 0:
            print('Error: Ingrese un número par.')
        else:
            agregar_una_vez(Lista_pares, num)
    except ValueError:
        print('Ingrese un numero valido. ')
print(f'La lista de números pares es: {Lista_pares}')
print()

while True:
    entrada = input('Ingrese multiplos de 4 para agregar a la lista: \n(0 para finalizar): ')
    try:
        num = int(entrada)
        if num == 0:
            break
        if num % 4 != 0:
            print('Error: Ingrese un multiplo de 4.')
        else:
            agregar_una_vez(Lista_multiplos4, num)
    except ValueError:
        print('Ingrese un numero valido. ')
print(f'La lista de los mutiplos de 4 es: {Lista_multiplos4}')
print()

while True:
    try:
        entrada = input('Ingrese el nombre de un aprendiz para agregar a la lista: \n("fin" para finalizar): ')
        if entrada == 'fin':
            break
        if not entrada.isalpha():
            raise ValueError('Error: Solo puede ingresar palabras. ')
        Lista_2693630.append(entrada.upper())
    except ValueError as error:
        print(error)
        continue
print(f'La lista de las letras es: {Lista_2693630}')
print()

while True:
    try:
        entrada = input('Ingrese una letra para agregar a la lista: \n("fin" para finalizar): ')
        if entrada == 'fin':
            break
        if len(entrada) != 1 or entrada.isnumeric():
            raise ValueError('Error: Solo puede ingresar una letra.')
        Lista_solo_letras.append(entrada.upper())
    except ValueError as error:
        print(error)
        continue
print(f'La lista de las letras es: {Lista_solo_letras}')
print()