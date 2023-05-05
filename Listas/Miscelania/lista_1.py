#Imprimir la suma, el promedio, el numero mayor, el numero menor...
#La moda, la mediana y la desviacion extandar de una lista aleatoria.
import math
import random
sum=0
prom=0
mayor=0
menor=101
moda=0
resta=0
division=0
raiz=0
moda=0
mediana=0

lista=[]
tam=random.randint(10,20)
print (f'En la lista hay {tam} elementos: ')
for i in range (tam):
    num=random.randrange(100)
    lista.append(num)
print(lista)
print ()

#Suma de los numeros de la lista.
for numeros in lista:
    sum += numeros
print (f'La suma total es: {sum}')

#Promedio de los numeros de la lista.
for numeros in lista:
    prom = sum//tam
print (f'El promedio es: {prom}')

#Numero mayor y menor de la lista.
for numeros in lista:
        if numeros>mayor:
            mayor=numeros
        if numeros<menor:
             menor=numeros
print(f'El numero mayor es: {mayor} ')
print(f'El numero menor es: {menor} ')

#Mediana de los numeros de la lista.
if tam % 2 == 0:
     num1 = tam // 2
     num2 = num1 -1
     mediana = (lista[num1]+lista[num2]) // 2
     print(f'La mediana es: {mediana}')
else:
    num_imp = tam // 2
    mediana = (lista[num_imp])
    print(f'La mediana es: {mediana}')

#Moda de los numeros de la lista.
max = 0
for num in lista:
    cont = 0
    for s in lista:
        if num == s:
            cont +=1
    if cont > max:
        max = cont 
        moda =num
print (f'La moda es: {moda}')

#Desviacion extandar de los numeros de la lista.
for numeros in lista:
     numeros = resta - (sum) / (prom)
     cuadrado = resta ** 2
     sum += cuadrado
     division = sum / prom
raiz = math.sqrt (division)
print(f'La desviacion extandar es: {raiz} ')

#Orden ascendente
for i in range(tam-1):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            lista[i],lista[j]=lista[j],lista[i]
print('El orden de la lista de menor a mayor es:')
print (lista)
print()

#Orden descendente
for i in range(tam-1):
    for j in range(i+1,tam):
        if lista[i]<lista[j]:
            lista[i],lista[j]=lista[j],lista[i]
print('El orden de la lista de mayor a menor es: ')
print (lista)