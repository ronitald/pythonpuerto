#Ingresar numeros, hasta que desee finalizar con el 0.
#Mostrar cuantos numeros fueron ingresador.
#Mostrar la suma de los numeros ingresados.
#Mostrar el promedio de los numeros ingresados.
#Mostrar cual es el mayor y el menor de los numeros ingresados.

#Definicion de variaables.
num=1
cont=0
sum=0
menor=1000000 #Numero maximo.
mayor=0

#Condicicional, Ingresar cualquier numero, con el 0 finaliza.
while num!=0:
    num=int(input('Ingrese un numero: '))
    cont=cont+1 #Contador incrementa en uno.
    sum=sum+num #Suma de las variables.
    if num>mayor:
        mayor=num
    if num<menor and num!=0:
        menor=num

print(f'Ingreso {cont-1} numeros. ')
print(f'La suma es {sum}')
print(f'El promedio es {sum/(cont-1)}')
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')