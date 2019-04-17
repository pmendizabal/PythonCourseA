print("Programa que evalua a los alumnos")

nota_alumno=input("Introduce la nota del alumno: ") #Recuerda que python siempre reconoce el input como texto

def evaluacion(nota):
	valoracion="Aprobado"
	if nota<=5:
		valoracion="suspenso"
	return valoracion

#print(evaluacion(8))

print(evaluacion(int(nota_alumno)))