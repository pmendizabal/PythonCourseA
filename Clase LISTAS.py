miLista=["sachiel", "adan", "lilith", "shamshiel"] #corchete

#Comienza desde cero
#print(miLista[:])

print(miLista[0])

print(miLista[-1])

print(miLista[0:3]) #se excluye el 3

print(miLista[2:]) #acceder a los dos ultimos elementos

print(miLista[:3]) #lo mismo con el cero a la izquierda

miLista.append("Londe") #para insertar otro valor al final de la cadena

print(miLista[:])

miLista.insert(3,"Squirtle") #solo para definir un espacio especifico

print(miLista[:])

miLista.extend(["pikachu","charmander","charizard"]) #es obvio la funcion

print(miLista[:])

print(miLista.index("Londe")) #esto es mas practico, nos dice el lugar

print("febas" in miLista) #afirmar si el elemento esta contenido en la lista

miLista.remove("Londe")

print(miLista[:])

miLista.pop() #Elimina el ultimo elemento

print(miLista[:])

miLista2=["raichu", "loudred"] * 3  #con esto, se imprime la lista 3 veces

miLista3=miLista+miLista2

print(miLista3[:])

print(miLista2[:])

