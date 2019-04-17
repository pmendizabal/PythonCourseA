"""
HERENCIA

Existe una clase padre (superclase) ya que engloba a un determinado
numero de clases. Ahora, tambien hay otra clase que es subclase y
superclase a la vez porque engloba a otras clases.

La utilidad es reutilizar codigo en caso de crear objetos similares:
¿que caracteristicas en comun tienen los objetos a crear?
Marca, modelo
¿que comportamientos en comun tienen todos los objetos?
arrancan, aceleran, frenan

"""

class Vehiculos():

	def __init__(self, marca, modelo):
		
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		
		self.enmarcha=True

	def acelerar(self):
		
		self.acelera=True

	def frenar(self):
		
		self.frena=True

	def estado(self):
		
		print("Marca; ", self.marca, "\nModelo: ",self.modelo,
		    "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", 
		    self.acelera, "\nFrenando: ", self.frena) #con el \n hacemos un salto de renglon


class Moto(Vehiculos): #con esto ya se heredo la clase padre Vehiculos
   pass

miMoto=Moto("Honda", "CBR")

miMoto.estado()

