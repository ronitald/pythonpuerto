inicio=0
fin=int(input('Ingrese el numero de fin: '))
n=int(input('Ingrese un multiplo: '))

contador=0
for i in range (inicio, fin+1):
    print (i)

contador=0
for i in range (fin+1):
    if i % n == 0:
        contador = + contador +1
print(f'En la serie hay {contador} multiplos de {n}')