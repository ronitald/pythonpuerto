
#1 solo argumento es el inicio.
for i in range(11):
    if i%3==0: #Verificar si es multiplo de 3
        print(f'{i} es multiplo de 3')
    else:
        print(i)

#2 argumentos indica el inicio y el fin.
for j in range(1,11):
    print(j)

#3 argumentos indica el inicio, fin, incremento 
for k in range(0,11,2):
    print(k)

#3 argumentos indica el inicio, fin, decremento
for i in range(20,0,-2):
    print(i)