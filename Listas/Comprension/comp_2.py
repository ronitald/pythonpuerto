import random
import math

tam = random.randint(5, 10)
lista = [random.randrange(100) for i in range(tam)]
lista2 = [i for i in lista]
exponente = 2
potencia = [x ** exponente for x in lista if x % 2 != 0]
raices = [round(math.sqrt(x), 2) for x in lista2 if x % 2 == 0]

print(lista)
print(f'La potencia de los números impares es: {potencia}')
print(f'La raíz de los números pares es: {raices}')
