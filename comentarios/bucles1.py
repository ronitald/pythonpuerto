#Asignacion de variables
#Contador
i=1  

sum=0 #Contador de la suma, una variable que es igual a la misma variable mas una constante.

#El ciclo finaliza hasta que calcule los numero menores o iguales a 5.
while i<=5:
    print(i)
    sum=sum+i 
    i+=1 #Se incrementa en uno

print(f'la suma es ={sum}')