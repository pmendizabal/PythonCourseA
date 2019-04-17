"""Diccionarios
Permiten almacenar valores de diferente tipo (int,float, etc)
e incluso listas y otros diccionarios.
Los datos se almacenan asociados a una clave de tal 
forma que se crea una asociacion de tipo clave:valor 
para cada elemento almacenado.
Los elementos almacenados no estan ordenados.
"""

midiccionario={"Alemania":"Berlín","Francia":"Paris","UK":"Londres"}

print(midiccionario)
print(midiccionario["Francia"])

midiccionario["Italia"]="Lisboa"

print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)

del midiccionario["UK"] #Eliminar elemento
print(midiccionario)

midiccionario2={"Alemania":"Berlín", 23:"Jordan", "Mosqueteros":3}

print(midiccionario2)

mitupla=("Espagna", "Francia", "UK", "Alemania")
midiccionario3={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlín"}

print(midiccionario3)
print(midiccionario3["UK"])

datos_jordan={23:"Jordan", "nombre":"Michael", "Equipo":"Chicago", "anillos":
  {"temporadas":(1991,1992,1993,1997)}}

print(datos_jordan)
print(datos_jordan["anillos"])

print(datos_jordan.keys()) #te da las claves
print(datos_jordan.values()) #lo contrario
print(len(datos_jordan)) #tamaño de los valores
