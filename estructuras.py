"""
<<<<<<< HEAD
[] corchetes
{} llaves
() parentesis
<> parentesis angular
=======
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
<<<<<<< HEAD

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
=======
>>>>>>> 24f878dd85d93de9dda5a73ff910689c608a59ed
"""

#Listas
###################################
#           Definición      []    #
###################################
frutas1= ["pera","mango","papaya"]
frutas2= list() 
###################################
print("Lista:",frutas1[1])
###################################
#           Modificar      []     #
################################### 
frutas2.append("coco")
frutas2.append("kiwi")
frutas1.extend(frutas2)
print("Agregado a lista:",frutas1)
###################################
#           operaciones    []     #
###################################
print("posición del coco:",frutas1.index("coco")) # devuelve la posición


frutas1.insert(3,"fresa") # ingresar un valor en posición especifica
print("ingresar en posición 3:",frutas1[3] )

frutas1.remove("fresa")
print("remover en posición 3:",frutas1[3] )

frutas1[3]="banano"
print("modificar:",frutas1)


print("pop:",frutas1.pop(3))
print(frutas1)
###################################
#           recorrerlo     []     #
###################################
print("############recorrido lista###############")
for fruta in frutas1:
    print(fruta)
print("###########################")

#Diccionarios
###################################
#           Definición      {}    #
###################################
canasta1={"bolsa1":["pera","mango","papaya"],
         "bolsa2":5}
canasta2= dict()
##################################
print("Dicionario:",canasta1["bolsa1"])

print("Dicionario:",canasta1["bolsa1"][2]) #si quisiera acceder a un elemento en especifico de la lista 
###################################
#           operaciones    {}     #
###################################
print("listar llaves:",canasta1.keys())
print("listar valores:",canasta1.values())
print("listarlos tupla:",canasta1.items())
print("Existe bolsa2","bolsa2" in canasta1)

canasta1["bolsa3"]= False
print("agregar a diccionario:", canasta1)
###################################
#           recorrerlo     {}     #
###################################
print("############recorrido diccionario###############")
for key in canasta1:
    print(key)
print("###########################")
#Tuplas
###################################
#           Definición            #
###################################
tiempos=(5,3,4)
t=(1,)
print("Tipo:",type(t))
##################################
print("Tupla:",tiempos[1])


#Conjuntos(Set)
###################################
#           Definición            #
###################################
lista=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
print("Ejemplo de uso set:", set(lista))

#String
###################################
#           Definición            #
###################################
palabra= "hola mundo!"
palindromo="Reconocer"
print("String:",palabra[0])
print("String:",palabra[:3])
print("String:",palabra[3:])
print("String:",palabra[-1])
print("String:",palabra[::2])
print("String:",palabra[::-1])
print("String:",palindromo[::-1])





>>>>>>> ca7b88f141c145a1aafb9308ad6fd8ec5c6906f0
