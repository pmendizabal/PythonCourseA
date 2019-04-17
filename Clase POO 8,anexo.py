class Persona():

	def __init__(self, nombre, edad, Lugar_residencia):

		self.nombre=nombre

		self.edad=edad

		self.lugar_residencia=Lugar_residencia

	def descripcion(self):
		
		print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", 
			self.lugar_residencia)

class Empleado(Persona):

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
		#Ahora para no trabajar con datos que le damos, podemos poner mas argumentos aqui para jalar la informacion
		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

		#super().__init__("Antonio", 55, "España") #Con esto, almacena el init inicial y solo basta darle los argumentos especificos

		self.salario=salario

		self.antiguedad=antiguedad

	def descripcion(self):
		
		super().descripcion()

		print(" Salario: ",self.salario," Antiguedad: ", self.antiguedad)

Antonio=Persona("Antonio", 55, "España")

Jorge=Empleado(1500, 15, "Jorge", 55, "Colombia")

Antonio.descripcion()

Jorge.descripcion()

"""
El principio de sustitucion significa si es siempre un/a determinada
cosa. Sirve para verificar si la herencia esta bien implementada.
La funcion isinstance() sirve para esto.

"""

print(isinstance(Jorge, Empleado)) #Se corrobora la informacion en 49 y 51

print(isinstance(Jorge, Persona))

print(isinstance(Antonio, Empleado)) 
