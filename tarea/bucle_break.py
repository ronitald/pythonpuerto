num = int(input("Ingrese un número: "))
suma = 0
for i in range(1, num + 1):
    suma += i
    if suma > 100:
        break
else:
    print("La suma de los números enteros desde 1 hasta", num, "es:", suma)
    if suma <= 100:
        print("La suma es menor o igual a 100.")