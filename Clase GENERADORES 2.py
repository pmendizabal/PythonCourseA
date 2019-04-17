def devuelve_ciudades(*ciudades): #el parentesis significa que va a recibir un deteminado numero de argumentos en tupla

   for elemento in ciudades:
   	 #for subElemento in elemento: #para no anidar se utiliza yield from
   	 	yield from elemento



ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))