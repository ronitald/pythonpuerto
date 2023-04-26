#Verificar que dos numeros sean factores entre si.
#Definicion de variables.
x,y=3,5

cont=1 #Incremento del contador en uno.

#Verificar que los dos numeros sean factores...
#Sin importar su orden.
while not(x%y==0 or y%x==0): 
    print(f'Intento numero:  {cont}')
    x=int(input('Ingrese un numero: '))
    y=int(input('Ingrese un numero: '))
    cont+=1

print(f'{x} y {y} son factor. ')