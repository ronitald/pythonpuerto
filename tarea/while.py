import random
secreto = random.randint(1, 100)
adivinado = False
while not adivinado:
    num = int(input("Adivine el número secreto: "))
    if num == secreto:
        print("¡Felicidades, adivinaste el número!")
        adivinado = True
    elif num < secreto: 
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
