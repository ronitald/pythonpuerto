num = int(input("Ingrese un número: "))
suma = 0
for i in range(1, num + 1):
    if i % 3 == 0:
        continue
suma += i
print("La suma de los números enteros desde 1 hasta", num, "sin contar los múltiplos de 3 es:", suma)
