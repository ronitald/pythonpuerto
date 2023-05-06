import random

n = 10
lista = []

while len(lista) < n:
    num = random.randint(1, 50)
    if num not in lista:
        lista.append(num)
    else:
        print(f'El numero {num} ya esta en la lista. ')
print(lista)
