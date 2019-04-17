"""
for letra in "Python":

	if letra=="h":
		continue   #ignora la linea de codigo que se ordena


	print("Viendo la letra: " + letra)
"""


"""
nombre="Pildoras Informaticas"

contador=0

for i in nombre:

	if i==" ":
		continue   #Con este pequeño bucle podemos rescindir del espacio como caracter
	contador+=1  #Lo aumenta en 1

#print(len(nombre))

print(contador)  #esto es otra manera de contabilizar utilizando un bucle

"""

"""
while True:
	pass #con ctrl+c rompes el bucle infinito, pass se utiliza para volverlo nulo
"""

email=input("Introduce tu email: ")

for i in email:

	if i=="@":

		arroba=True

		break;

else:

	 arroba=False

print(arroba)

