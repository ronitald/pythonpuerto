import random

def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

lista1=llenarLista(5,20)

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def mayor(lista):
    maximo = 0
    for x in lista:
        if x > maximo:
            maximo = x
    return maximo

def menor(lista):
    minimo = 1000
    for x in lista:
        if x < minimo:
            minimo = x
    return minimo

def ordenasc(lista1):
    for i in range(len(lista1) - 1):
        for j in range(i + 1, len(lista1)):
            if lista1[i] > lista1[j]:
                lista1[i], lista1[j] = lista1[j], lista1[i]
    return lista1

def ordendes(lista1):
    for i in range(len(lista1) - 1):
        for j in range(i + 1, len(lista1)):
            if lista1[i] < lista1[j]:
                lista1[i], lista1[j] = lista1[j], lista1[i]
    return lista1

print()
print(lista1)
print(f'La suma de la lista es: {sumaLista(lista1)}')
print(f'El promedio es: {promedioLista(lista1)}')
print(f'El numero mayor es: {mayor(lista1)}')
print(f'El numero menor es: {menor(lista1)}')
print(f'El orden ascendete de la lista es: {ordenasc(lista1)}')
print(f'El orden descendente de la lista es: {ordendes(lista1)}')
print()