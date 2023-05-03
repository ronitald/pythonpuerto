cont=0 
num=1
while num>=0:
    num=int(input("Escriba un numero positivo: "))
    if num>=0:
        cont+=1
    else: 
        print(f"Usted ingreso {cont} numeros positivos") 