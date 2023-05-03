n = int(input("Escriba un numero positivo: "))
for i in range(n, 0, -1):
    for h in range(1, i+1, +1):
        print(h, end="")
    print()