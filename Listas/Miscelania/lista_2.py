num = int(input('Escriba los digitos para finalizar la serie de Fibonacci: '))

lista = [0, 1]

# Calcular los siguientes números de la serie de Fibonacci hasta que el último tenga la cantidad de dígitos indicada por el usuario
while len(int(lista[-1])) < num:
    num2 = lista[-1] + lista[-2]
    lista.append(num2)

print(lista)
    