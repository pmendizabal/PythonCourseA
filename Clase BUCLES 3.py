#El primer argumento se refiere al numero de elementos, con el segundo argumento
#solo dictas hasta donde llega la serie (donde comienza y donde finaliza) y con
#el tercer argumento dictas de cuanto en cuanto va saltando la serie


"""
for i in range(5, 10, 2):   
	print(f"valor de la variable {i}")
"""


#Hay que hacer que el programa acepte mas de un punto como valido *PENDIENTE
valido=False

email=input("Introduce email: ")
puntito="."
punt=int(puntito>1)

for i in range(len(email)):

	if email[i]=="@" and email[i]==punt:
		valido=True

if valido:

	print("Email correcto")
else:

	print("Email incorrecto")