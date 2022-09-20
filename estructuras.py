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

#Tuplas
###################################
#           Definición            #
###################################
tiempos=(5,3,4)

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





