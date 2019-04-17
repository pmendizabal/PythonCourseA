from io import open

archivo_texto=open("arhivo.txt","r")

#archivo_texto.seek(0)

#El puntero se refiere al cursor dentro del archivo de texto,
#con el metodo seek podemos ubicar el puntero donde queramos:

#print(archivo_texto.read(11))

#Con seek, se coloca el puntero en donde le indicamos y empieza a leer
#pero con read, solo lee los primeros 11 caracteres que le indicamos:


#print(archivo_texto.read())

#Al hacer la linea 15, se lee lo que sigue de los 11 caracteres


"""
#Con las siguientes lineas, solo partimos el texto y leer a partir de ahi
archivo_texto.seek(len(archivo_texto.read())/2)

print(archivo_texto.read())
"""

archivo_texto=open("arhivo.txt","r+")  #Con r+ nos referimos a lectura y escritura

archivo_texto.write("Comienzo del texto")

#Con esto, lo que escribamos lo podemos ubicar en cualquier parte del texto,
#en este caso, desde la primera posicion ya que no espeficicamos nada

lista_texto=archivo_texto.readlines()

lista_texto[2]="Esta linea ha sido incluida"

#Y con esto podemos introducir texto por lineas y no caracteres

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()
