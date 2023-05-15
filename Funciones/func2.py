import random

def llenarLista(tam, rango):
    lista = [random.randrange(rango) for i in range(tam)]
    return lista

lista1 = llenarLista(5, 10)
lista2 = llenarLista(5, 10)

def suma(lista):
    sum = 0
    for x in lista:
        sum += x
    return sum

def sumaAlta(lista1, lista2):
    sumalista1 = suma(lista1)
    sumalista2 = suma(lista2)

    if sumalista1 > sumalista2:
        return "La lista 1 tiene la suma mas alta. "
    elif sumalista1 < sumalista2:
        return "La lista 2 tiene la suma mas alta. "
    else:
        return "Las dos listas tienen la misma suma. "

def mayor(lista1, lista2):
    mayorlista1 = max(lista1)
    mayorlista2 = max(lista2)

    if mayorlista1 > mayorlista2:
        return f"El numero mayor es {mayorlista1} de la lista 1. "
    elif mayorlista1 < mayorlista2:
        return f"El numero mayor es {mayorlista2} de la lista 2."
    else:
        return f"Ambas listas tienen el mismo número mayor {mayorlista1}. "

def menor(lista1, lista2):
    menorlista1 = min(lista1)
    menorlista2 = min(lista2)

    if menorlista1 < menorlista2:
        return f"El numero menor es {menorlista1} de la lista 1. "
    elif menorlista1 < menorlista2:
        return f"El numero menor es {menorlista2} de la lista 2."
    else:
        return f"Ambas listas tienen el mismo número menor {menorlista1}. "

def promlista1(lista1):
    return suma(lista1) / len(lista1)

def promlista2(lista2):
    return suma(lista2) / len(lista2)

def promlistas(lista1, lista2):
    return round((promlista1(lista1) + promlista2(lista2)) / 2, 2)

print()
print(f'1: {lista1}')
print(f'2: {lista2}')
print(f'Suma Lista 1: {suma(lista1)}')
print(f'Suma Lista 2: {suma(lista2)}')
print(sumaAlta(lista1, lista2))
print(mayor(lista1,lista2))
print(menor(lista1,lista2))
print(f'El promedio conjunto es: {promlistas(lista1,lista2)}')
print()