"""
Consiste en guardar en un fichero externo una coleccion, diccionario o un 
objeto pero se guardara en un fichero externo codificado de forma binaria.
El proposito es de flexibilizacion en todos los entornos que queramos 
manejar dicha informacion.
Para usar esto hay que utilizar la biblioteca Pickle, con el metodo
dump y load
"""

#El siguiente proceso  es para generar el fichero y guardarlo

import pickle
"""
lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario=open("lista_nombres", "wb") #writing binary

pickle.dump(lista_nombres, fichero_binario) #El primer argumento es lo que queremos guardar

fichero_binario.close()

del (fichero_binario)
"""

fichero=open("lista_nombres", "rb")

lista=pickle.load(fichero)

print(lista)