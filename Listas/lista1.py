#Imprimir la suma, el promedio, el numero mayor, el numero menor...
#La moda, la mediana y la desviacion extandar de una lista aleatoria.
import random
sum=0
prom=0
mayor=0
menor=101
moda=0
lista=[]
tam=random.randint(10,20)
print (f'En la lista hay {tam} elementos: ')
for i in range (tam):
    num=random.randrange(100)
    lista.append(num)
print(lista)
print ()

for numeros in lista:
    sum += numeros
print (f'La suma total es: {sum}')

for numeros in lista:
    prom = sum//tam
print (f'El promedio es: {prom}')

for numeros in lista:
        if numeros>mayor:
            mayor=numeros
        if numeros<menor:
             menor=numeros
print(f'El numero mayor es: {mayor} ')
print(f'El numero menor es: {menor} ')

