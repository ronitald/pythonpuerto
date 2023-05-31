import random

def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

lista1=llenarLista(5,20)
