#Imprimir numero del 1 hasta el que ingreso el usuario.
#Mostrar cuando hay un multiplo de 7.

#Definicicion de variables.
num = int(input("Ingrese un número: "))
i = 1

while i <= num:
    if i % 7 == 0: #Verificar cuales numeros son multiplos de 7.
        print(i, "Es múltiplo de 7")
    else:
        print(i)
    i += 1 #Contador incrementa en uno.
