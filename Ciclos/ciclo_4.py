nump=int(input("Ingrese un numero: "))
for i in range(2, nump+1):
    a=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            a= a+j
    if(a==i):
        print(f"{i} es perfecto")
    else:
        print(f"{i} no es perfecto")