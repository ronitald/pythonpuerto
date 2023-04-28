while True:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    if num1 > num2:
        break
    print("El primer numero debe ser mayor que el segundo.")
    print("Inténtalo de nuevo.")

resultado = num1 - num2
if resultado > 0:
    print(f"La resta de los dos numeros es igual a {resultado}")
    while resultado > 0:
        num3 = int(input("Introduce otro número para seguir restando: "))
        resultado -= num3
        if resultado > 0:
            print(f"Quedan {resultado} unidades por restar")
        else:
            print("Ya no se pueden restar más unidades.")
else:
    print(f"La resta de los dos numeros es igual a {resultado}.")
    print("No se pueden restar más unidades.")