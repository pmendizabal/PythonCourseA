"""
Objetivo: Posibilidad de guardar datos del programa para que no se pierdan,
podemos guardar los datos en archivos externos o en bases de datos BBDD.
Fases para guardar info en archivos externos:
1.-Creacion
2.- Apertura
3.- Manipulacion
4.- Cierre

Para esto hay que utilizar el modulo io

"""

from io import open

"""
archivo_texto=open("arhivo.txt","w") 
#el archivo lo podemos abrir en modo lectura o escritura o append
#el argumento w significa de escribir

frase="Estupendo dia para estudiar python \n el jueves"

#Esto para incorporar la frase a nuestro archivo, el argumento es el objeto frase
archivo_texto.write(frase)

archivo_texto.close() #Hay que cerrar el archivo desde la consola
"""

"""
archivo_texto=open("arhivo.txt","r") 


texto=archivo_texto.read()

archivo_texto.close()

print(texto)


#Con readlines podemos hacer que un archivo se vuelva una lista
lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto[0])

#Entonces, cada linea de texto se vuelve un miembro de la lista.
#Para elegir una linea especifica solo basta con introducir el
#numero del miembro de la lista entre corchetes
"""

archivo_texto=open("arhivo.txt","a")

archivo_texto.write("\n siempre es una buena ocasion para estudiar")

archivo_texto.close() 


