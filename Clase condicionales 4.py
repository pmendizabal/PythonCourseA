"""print("Programa de becas 2018")

distancia_escuela=int(input("Introduce la distancia que recorres a la escuela en km: "))
print(distancia_escuela)

num_hermanos=int(input("Introduce el numero de hermanos: "))
print(num_hermanos)

salario_familiar=int(input("Introduce salario mensual bruto: "))
print(salario_familiar)

#Solo recuerda los operadores logicos "and" y "or"
if distancia_escuela>40 and num_hermanos>2 and salario_familiar<=20000:

  print("Tienes una beca de 300 pesos")

else:

	print("No debes tener beca") """


"""
print("Asignaturas optativas 2017")

print("Informatica - Pruebas de software - Pruebas - Usabilidad")

asignatura=input("Escribe la asignatura escogida: ")

if asignatura in ("Informatica", "Pruebas de software", "Pruebas", "Usabilidad"):

	print("Asignatura elegida " + asignatura)
else:

	print("La asignatura no esta libre") """

#Pero el programa debe reconocer entre mayusculas y minusculas, entonces

print("Asignaturas optativas 2017")

print("Informatica - Pruebas de software - Pruebas - Usabilidad")

opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower() #se transformo lo que sea a minusculas

if asignatura in ("informatica", "pruebas de software", "pruebas", "usabilidad"):

	print("Asignatura elegida " + asignatura)
else:

	print("La asignatura no esta libre")