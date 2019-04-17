
"""
def evaluaEdad(edad):

	if edad<0:
		raise TypeError("No existen edades negativas") #con raise se provoca la excepcion
        #De igual forma, no puedes inventar un error, solo las clasificadas
        #Pero si se puede crear una clase con un error
	elif edad<20:
		return "Eres joven"
	elif edad<40:
		return "Eres menos joven"
	elif edad<65:
		return "Eres maduro"
	elif edad<100:
		return "cuidate"

print(evaluaEdad(-10))

"""

import math

def calculaRaiz(num1):

	if num1<0:
		raise ValueError ("No puede ser negativo")

	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un numero: ")))

try:
  print(calculaRaiz(op1))

except ValueError as ErrordeNumeroNegativo:

   print (ErrordeNumeroNegativo)

print("Fin")

