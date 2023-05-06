num = int(input('Escriba los digitos para finalizar la serie de Fibonacci: '))

lista = [0, 1]

while len(str(lista[-1])) < num:
    num2 = lista[-1] + lista[-2]
    lista.append(num2)

print(lista)
    