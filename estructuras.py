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

x = 5
if 0 < x:
    if x < 10:
        print("x es un numero positivo de un solo dígito.")  # no recomendable

if 0 < x and x < 10:
    print("x es un numero positivo de un solo dígito.")  # recomendable

if 0 < x < 10:
    print("x es un numero positivo de un solo dígito.")  # recomendable
