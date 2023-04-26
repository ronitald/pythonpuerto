#El programa permitira mostrar el mayor de 3 numeros ingresados por el usuario
#Asignacion de variables
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

#Primera condicion, si no se cumple, continuara con el else
if num1 >= num2:
    if num1 >= num3: #No se cumplira si no se cumple la primera condicion.
        print("El número más grande es: ",num1) #Indentacion(Sangria)
    else: #Si la condicion anterior no se cumplio esta si se cumplira.
        num2 >= num3
        print("El numero mas grande es: ",num3)
else: #Solo se cumplira si el primer if no se cumple.
    if num2 >= num3:
        print("El numero mas grande es: ",num2)