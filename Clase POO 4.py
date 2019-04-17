class Coche():

	def __init__(self):  #de esta forma se especifica el constructor

	   self.__largoChasis=250  # tiene 4 propiedades
	   self.__anchoChasis=120
	   self.__ruedas=4  #se utiliza dos guiones bajos para encapsular y no es accesible desde fuera
	   self.__enmarcha=False 

	#Vamos a crear un metodo

	def arrancar(self,arrancamos):

	    self.__enmarcha=arrancamos

	    if(self.__enmarcha):
	    	chequeo=self.__chequeo_interno()

	    if(self.__enmarcha and chequeo):
	       return "El coche esta en marcha" # hay 2 comportamientos

	    elif(self.__enmarcha and chequeo==False):
	       return "Algo ha ido mal en el chequeo"

	    else:

	      return "El coche esta parado"    
	        #hace referencia al propio objeto perteneciente a la clase
	        #con el nuevo argumento "arrancamos" queremos que nos diga el estado
		  

	def estado(self):
		#ahora queremos que estado nos diga las propiedades
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", 
			self.__anchoChasis, " y un largo de ", self.__largoChasis)


	def __chequeo_interno(self):  #encapsulamos el metodo para que linea 61 no ocurra
		print("Realizando chequeo interno")

		self.gasolina="OK"
		self.aceite="OK"
		self.puertas="Cerradas"

		if(self.gasolina=="OK" and self.aceite=="OK" and self.puertas=="Cerradas"):

		    return True

		else:

			return False
			

miCoche=Coche()  #Instanciar una clase, ejemplar de clase


print(miCoche.arrancar(True)) #de esta forma, se aplica el metodo. Pero ahora hay que especificar el argumento dado que lo generamos

miCoche.estado()


print("------------A continuacion creamos el segundo objeto----------")

#se crea segunda instancia

miCoche2=Coche()

print(miCoche2.arrancar(False))

#miCoche2.__ruedas=5  aqui modificamos una propiedad inicial, el programa funciona pero no debe suceder esto, entonces aplicamos la encapsulacion

miCoche2.estado()


#Es comun que las propiedades comunes de los objetos formen parte de un
#estado inicial, entonces se crea un constructor que es el que le da
#un estado inicial a los objetos

#Recuerda que al poner los dos guiones bajos, se marcan como cosas diferentes
#si no los pusieras con estos