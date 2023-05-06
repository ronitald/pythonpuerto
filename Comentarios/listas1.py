#[] listas, {} diccionarios, () tuplas, {()}   
x=100
print(type(x))
x='Soacha'
print(type(x))
lista=['python',100,[1,2,3,[]],'a']  #Definicion de elementos de la lista.
print(type(lista))
print(len(lista)) #Funcion len, muestra la cantidad de elementos de la lista.
print(lista[0]) #Imprimir el primer elemento de la lista
print(lista[1]) #Imprimir el segundo elemnto de la lista.
print(lista[3]) #Imprimir el cuarto elemento de la lista.
print(lista[-4]) #Se usa el menos para eliminar un elemento de atras hacia delante.

del lista[-2] #Del, se usa para eliminar un elemento especifico de la lista.
print(lista)

"""
cuenta1=cuenta()
cuenta2=cuenta()
cuenta3=cuenta()
cuenta1.deposit()
print(type(cuenta1))
cuenta2.deposit()
cuenta3.deposit()
"""