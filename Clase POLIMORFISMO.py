"""
El polimorfismo solo se refiere que un objeto puede
cambiar de forma, o sea, cambia sus propiedades y
funciones.
"""

class Coche():

	def desplazamiento(self):
		print("Me desplazo utilizando 4 ruedas")

class Moto():

	def desplazamiento(self):
		print("Me desplazo utilizando 2 ruedas")

class Camion():

	def desplazamiento(self):
		print("Me desplazo utilizando 6 ruedas")


"""
miVehiculo=Moto()

miVehiculo.desplazamiento()

miVehiculo2=Coche()

miVehiculo2.desplazamiento()

miVehiculo3=Camion()

miVehiculo3.desplazamiento()

Entonces hemos creado 3 objetos que aluden a clases distintas pero tienen
el mismo metodo. Podemos utilizar el polimorfismo

"""

def desplazamientoVehiculo(vehiculo): #el objeto vehiculo puede cambiar de forma dependiendo el contexto
	vehiculo.desplazamiento()

miVehiculo=Camion()

desplazamientoVehiculo(miVehiculo) #Con esto, el metodo nos ayuda a seleccionar lo correcto segun el objeto que hemos creado y definido
