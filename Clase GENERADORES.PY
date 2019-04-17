"""
Generadores

Estructuras que extraen valores de una funcion y se almacenan
en objetos iterables (que se pueden recorrer).
Estos valores se almacenan de uno en uno.
Cada vez que un generador almacena un valor, esta permanece en
un estado pausado hasta que se solicita el siguiente.
Esto se llama suspension de estado.

Ventajas:

Son mas eficientes que las funciones tradicionales.
Utiles con listas de valores infinitos.
Segun el contexto, es mejor que el generador devuelva los
valores de uno en uno.

"""

"""
Este es un codigo que ejemplifica como hacer un programa sin
generadores


def genPares(limite):

	num=1

	miLista=[]

	while num<limite:

		miLista.append(num*2)

		num=num+1

	return miLista

print(genPares(10))

"""

def generaPares(limite):

	num=1

	while num<limite:
		
		yield num*2

		num=num+1

devuelvePares=generaPares(10)

""" Con estas lineas salen nuestros numeros
for i in devuelvePares:

	print(i)

"""

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))