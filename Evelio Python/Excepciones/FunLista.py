num = 1
my_list = []

def agregar_una_vez(lista, elemento):
    try:
        if elemento in lista:
            raise ValueError('No se puede agregar un elemento duplicado')
        else:
            lista.append(elemento)
            return lista
    except ValueError as ve:
        print(f'Error: {ve}')
    except:
        print('Gracias por usar este programa')

while num != 0:
    entrada = input('Ingrese el número para agregar a la lista: ')
    try:
        num = int(entrada)
        print('Para finalizar, ingrese el número 0')
        agregar_una_vez(my_list, num)
    except ValueError:
        print('Error: Ingrese un número entero')

del my_list[-1]
print(f'La lista es: {my_list}')