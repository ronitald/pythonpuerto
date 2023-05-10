import random
import math

tam = random.randrange(20, 30)
notas = [round(random.random() * 5, 2) for i in range(tam)]

print()
aprobadas = [nota for nota in notas if nota >= 3]
print ('Las calificaciones aprobadas son: ')
print (aprobadas)
print ()

desaprobadas = [nota for nota in notas if nota < 3]
print ('Las calificaciones desaprobadas son: ')
print (desaprobadas)
print ()

rango1 = [x for x in notas if x < 2]
print('0 a 1:', rango1)
rango2 = [x for x in notas if 1 < x < 3]
print('1 a 2:', rango2)
rango3 = [x for x in notas if 2 < x < 4]
print('2 a 3:', rango3)
rango4 = [x for x in notas if 3 < x <= 5]
print('3 a 4:', rango4)
print()

promedio_aprobadas = sum(aprobadas) / len(aprobadas)
print(f"El promedio de notas aprobadas es: {promedio_aprobadas}")
print ()

promedio_desaprobadas = sum(desaprobadas) / len(desaprobadas)
print(f"El promedio de notas desaprobadas es: {promedio_desaprobadas}")
print()