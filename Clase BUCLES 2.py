"""
for i in ["pildoras", "informatica", 3]:

	print("Hola", end="") #para imprimir en una sola linea, puedes dejar espacios entre comillas y hace justo eso


for i in "juan@pildorasinformaticas.es": #aqui imprime tantas veces como haya strings

	print("Hola", end=" ")

"""


"""
email=False
miEmail=input("Introduce email: ")

for i in miEmail:

	if(i=="@"):

		email=True

if email==True:   #Incluso sin declarar que sea True, se considera True
   print("El email es correcto")
else:
	print("El email no es correcto")
"""


contador=0
miEmail=input("Introduce email: ")

for i in miEmail:

	if(i=="@" or i=="."):

		contador=contador+1

if contador==2:
	print("Email correcto")
else:
	print("Email no correcto")

#for i in range(5): #Esto solo si no se requiere especificar los elementos
#	print("Hola")
