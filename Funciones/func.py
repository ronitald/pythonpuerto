import random

def llenarLista(tam,rango):
    lista=[random.randrange (rango) for i in range(tam)]
    return lista

lista1=llenarLista(5,20)

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista (lista)/len(lista)

def mayor(lista1):
    for x in lista1:
        if x>mayor:
            mayor=x
    return mayor

print(lista1)
print(f'La suma de la lista es: {sumaLista(lista1)}')
print(f'El promedio es: {promedioLista(lista1)}')
print(f'El numero mayor es: {mayor(lista1)}')