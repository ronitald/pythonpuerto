import random  #Importar el módulo random para generar números aleatorios

#Crear dos listas vacías para almacenar datos.
lista=[]
cuadrado=[]
tam=random.randint(5,10)  #Generar un número aleatorio entre 5 y 10.
print(tam) #Tam imprime el tamaño de la lista.
for i in range(tam):
    num=random.randrange(100) #Llenar la lista con números aleatorios de 1 a 100.
    lista.append(num)
print(lista)

#Calcular los cuadrados de cada elemento en la lista.
for i in range(len(lista)):
    cuadrado.append(lista[i]**2)

#También se pueden utilizar otras formas de calcular los cuadrados:
    # lista[i]=lista[i]**2
    # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))

print(cuadrado)
print(sum(lista))