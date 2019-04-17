"""Tuplas

Son listas inmutables, no dinamicas, pero si se permiten extraer
porciones y busquedas.
Ventajas: rapidez, menos espacio, formatean strings, pueden
utilizarse como claves en un diccionario """

mitupla=("charmander",2,3,1999) #parentesis
miLista=list(mitupla) #para hacer lo contrario, solo usar la funcion tuple

print(miLista)
print(mitupla)
print("non" in mitupla)

print(mitupla)

print(mitupla.count(1999))  #contabilizar el elemento

print(len(mitupla))  #para saber el tamaño de la tupla (solo dice los elementos)

tupla_uni=("conste",)
print(len(tupla_uni))

#tambien se puede declarar como

mistuplas= "o",2,45

nombre, dia, mes, agno=mitupla #desempaquetado de tupla
print(nombre)
print(dia)
print(agno)
print(mes) 
