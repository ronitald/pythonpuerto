n=int(input("Introduce un numero positivo: "))
i=2
for num in range (2, 1001):
    while n % i != 0:
        i += 1
if i == n:
    print(f" {n} Es primo. ")
else: 
    print(f" {n} No es primo. ")