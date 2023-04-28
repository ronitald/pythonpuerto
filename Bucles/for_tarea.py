inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número de fin: "))
cantidad = int(input("Ingrese cantidad a incrementar o decrementar: "))

if cantidad > 0:
    for i in range(inicio, fin+1, cantidad):
        print(i)
else:
    for i in range(inicio, fin-1, cantidad):
        print(i)
