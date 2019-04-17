
"""
i=1

while i<=10:
	print("Ejecucion " + str(i))
	i=i+1

print("Fin")
"""


"""
edad=int(input("Introduce tu edad: "))

while edad<1 or edad>100:
	print("Esto no es correcto")
	edad=int(input("Introduce tu edad: "))

print("Thanks for collaborating")
print("Edad del aspirante " + str(edad))
"""


import math

print("Programa que calcula raiz cuadrada")
numero=int(input("Introduce un numero: "))

intentos=0

while numero<0:
	print("No es posible con este programa dicha accion")

	numero=int(input("Introduce un numero: "))
	if numero<0:
		intentos=intentos+1

	if intentos==2:
		print("Ya no hay mas intentos")
		break;

if intentos<2:
	solucion=math.sqrt(numero)  #esto es un paquete
	print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))