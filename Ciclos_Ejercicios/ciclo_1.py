num = int(input("Ingrese un numero: "))

for i in range (1, num, +1):
    if num%i==0:
        print(f"{i} es divisor de {num}")