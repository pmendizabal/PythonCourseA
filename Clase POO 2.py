class Coche():
	largoChasis=250  # tiene 4 propiedades
	anchoChasis=120
	ruedas=4
	enmarcha=False 

	#Vamos a crear un metodo

	def arrancar(self):  #hace referencia al propio objeto perteneciente a la clase
		self.enmarcha=True

	def estado(self):
		if(self.enmarcha):
			return "El coche esta en marcha" # hay 2 comportamientos
		else:
			return "El coche esta parado"

miCoche=Coche()  #Instanciar una clase, ejemplar de clase

print(miCoche.largoChasis)
print("El largo del coche es",miCoche.largoChasis)
print("El coche tiene ",miCoche.ruedas,"ruedas")

miCoche.arrancar() #de esta forma, se aplica el metodo

print(miCoche.estado())