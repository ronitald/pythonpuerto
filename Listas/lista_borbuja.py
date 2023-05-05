import random

lista = []
tam=random.randint(15,20)
print (f'En la lista hay {tam} elementos: ')
for i in range (tam):
    num=random.randint(0,10)
    lista.append(num)
print(lista)
print ()
veces=0

while True:
    num1 = int (input('Escriba un numero: '))
    if num1 in lista:
        print ('El numero si esta. ')
        break
    else:
        print ('El numero no esta, Intentalo denuevo... ')

for i in lista:
    if i == num1:
        veces += 1
print(f'El numero esta repetido {veces} vez. ')

for i in range(len(lista)):
    if num1 == lista[i]:
        print(f'{lista[i]} esta en la posicion {i}')