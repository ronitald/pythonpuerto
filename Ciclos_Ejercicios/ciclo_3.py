n=int(input("Ingrese un numero: "))
num1=6
num2=8
sum=0
for i in range (1, n):
    if n%i == 0:
        sum+=i
if sum==n: 
    print(f"{n} es un numero perfecto")
else:
    print(f"{n} no es numero perfecto")