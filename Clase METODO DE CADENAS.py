"""
Metodo de cadenas

Se necesita la manipulacion de caracteres alfanumericos.
Algunas funciones basicas son:
upper() -> Mayusculas todo
lower()
capitalize() -> La primera letra en mayus
count() Cuenta cuantas veces aparece una letra, una cadena, frase, en un texto
find() Nos dice la posicion donde aparece un caracter o cadena
isdigit() Nos dice si un valor introducido es una letra
isalum() Comprueba si es alfanumerico
isalpha() Comprueba si solo hay letras, no cuenta a los espacios
split() Separa por palabras utilizando espacios
strip() Borra espacios sobrantes al principio y al final 
replace() Cambia una palabra o una letra por otra
rfind() Lo mismo que find pero desde el final al principio

Busca "documentacion de python" y la primera pagina dale click,
ahora en "referencia de biblioteca", ahora en 2.1.5 y abajo aparece
"metodo de las cadenas", ahi aparece todo los metodos con sus argumentos

"""

nombreUsuario=input("Introduce un nombre de usuario: ")

print("El nombre es: ", nombreUsuario.upper())

print("El nombre es: ", nombreUsuario.lower())

edad=input("Introduce la edad: ")

#print(edad.isdigit())

while(edad.isdigit()==False):
    print("Introduce un valor numerico")

    edad=input("Introduce la edad: ")


if (int(edad)<18):

	print("No puede pasar")
else:
	print("Puede pasar")


"""
Tarea
Hacer programa que pida correo electronico y verifque que tenga arroba y 
en que posicion
"""