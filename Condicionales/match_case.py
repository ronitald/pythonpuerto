#Condicion que permitira reducir una cadena con varios condicionales, if, elif, else
#Asignacion de variables.
num1,num2=100,50
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')

#La variable op almacenara la operacion escogida.
op=int(input('¿Que operacion?'))  

#Se usa un case por cada operacion que puede pedir el usuario.
#Evitando usar cadenas anidadas de condicionales (if, elif, else).
match op:

    case 1:  
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)
    case 5:    
        print(num1%num2)