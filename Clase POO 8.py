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

class Furgoneta(Vehiculos):

	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta no esta cargada"


		


class Moto(Vehiculos): #con esto ya se heredo la clase padre Vehiculos
   hcaballito=""  #Con esto, describimos un comportamiento que es unico en Moto
   def caballito(self):
       self.hcaballito="Voy haciendo el caballito"
 
   def estado(self): #agregamos la propiedad especifica para las Motos en el mismo metodo
        print("Marca; ", self.marca, "\nModelo: ",self.modelo,"\nEn Marcha: ", 
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, 
        "\n", self.hcaballito)

class VElectrico(Vehiculos):
	def __init__(self, marca, modelo):

        super().__init__(marca, modelo)

		self.autonomia=100

	def cargarEnergia(self):

		self.cargando=True

miMoto=Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado() #Aqui se llama el ultimo metodo porque se sobreescribe


miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True)) #print para ver lo que esta sucediendo al poner True

class BicicletaElectrica(Vehiculos,VElectrico): #aqui heredamos de dos clases
  pass

#Inclusive si hay metodos con el mismo nombre, se privilegia el del primer metodo
"""
Ahora, hay dos formas para darle los argumentos de marca y modelo,
una seria ponerle los mismos argumentos a la clase y copiar todo lo
que esto implica. La otra es con la funcion super()
"""
miBici=BicicletaElectrica("Orbea","HT")