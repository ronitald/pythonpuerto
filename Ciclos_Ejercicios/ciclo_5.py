cont=0
for num in range (2, 1001):
    primo=1
    for i in range (2, int(num ** 0.5)+1):
        if num%i == 0:
           primo=0
    if primo:
        cont+=1 
        print(num ) 
print(f"Hay {cont} numeros primos")