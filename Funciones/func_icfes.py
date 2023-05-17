import random

def llenarLista():
    tam = random.randint(200, 2500)
    lista = [random.randint(100, 500) for _ in range(tam)]
    return lista

lista1 = llenarLista()

def ordenasc(lista):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def calculaCuartil(lista, cuartil):
    lista_ordenada = ordenasc(lista[:])
    calc_cuartil = int(cuartil * (len(lista_ordenada) + 1) / 4)
    return calc_cuartil

def calculaQuintil(lista, quintil):
    lista_ordenada = ordenasc(lista[:])
    calc_quintil = int(quintil * (len(lista_ordenada) + 1) / 5)
    return calc_quintil

def crearCuartil(lista, cuartil_valor):
    nuevo_cuartil = lista[:cuartil_valor]
    return nuevo_cuartil

def crearQuintil(lista, quintil_valor):
    nuevo_quintil = lista[:quintil_valor]
    return nuevo_quintil

def suma(lista):
    suma = 0
    for x in lista:
        suma += x
    return suma

def promedio(lista):
    return suma(lista) / len(lista)

lista_ordenada = ordenasc(lista1)
print(lista_ordenada)
print(f'El tamaño de la lista es: {len(lista1)}')

while True:
    cuartil = int(input('Escriba el número del cuartil a hallar (1-4): '))
    if cuartil <= 4:
        break
    else:
        print('Ingrese el numero nuevamente. ')

while True:
    quintil = int(input('Escriba el número del quintil a hallar (1-5): '))
    if quintil <= 5:
        break
    else:
        print('Ingrese el numero nuevamente. ')


print()
print(f'El cuartil {cuartil} está en la posición: {calculaCuartil(lista1, cuartil)}')
print(f'El promedio del cuartil es: {round(promedio(crearCuartil(lista1, calculaCuartil(lista1, cuartil))), 1)}')
print(f'El quintil {quintil} está en la posición: {calculaQuintil(lista1, quintil)}')
print(f'El promedio del quintil es: {round(promedio(crearQuintil(lista1, calculaQuintil(lista1, quintil))), 1)}')
print()