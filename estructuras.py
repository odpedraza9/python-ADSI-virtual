# El comando
"""
num = int(input("Ingrese un número:\n"))

if num == 100:
    print("Usted ecribió el 100")
elif num > 100:
    print("Usted escribió un número mayor a 100")
else:
    print("Usted escribió un número menor a 100")
"""
# Condicionales multiples
"""
x = 5
if 0 < x:
    if x < 10:
        print("x es un numero positivo de un solo dígito.")  # no recomendable

if 0 < x and x < 10:
    print("x es un numero positivo de un solo dígito.")  # recomendable

if 0 < x < 10:
    print("x es un numero positivo de un solo dígito.")  # recomendable

"""
"""
# ejercicio  
#El profesor le indica a Diego que durante el curso se sacaron 4 notas y todas tienen el mismo valor. Además le
#solicita que debe elaborar un programa que le ayude a calcular si aprobó o debe recuperar la materia no solo a él
#sino a todos sus compañeros.
#Para esto debe planificar correctamente un código en python que les ayude a automatizar este proceso.
"""
"""
nota1= 4.5
nota2= 2.9
nota3= 3.8
Nota4= 5.0

promedio= round((nota1+nota2+nota3+Nota4)/4.1)

if promedio >=3:
    print(f"su nota fue de {promedio}, usted Aprobo")
else:
    print(f"su nota fue de {promedio}, usted reprobo")
    
"""
corredor1 = 60
corredor2 = 45

if corredor1 < corredor2:
    print("El corredor 1 es mas rapido que el corredor 2")
else:
    print("El corredor 2 es mas rapido que el corredor 1")
print("el corredor mas rapid tuvo un tiempo de mi,"min(corredor1,corredor2))