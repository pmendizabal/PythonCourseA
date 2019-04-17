def divide():

	try:

	   op1=(float(input("Introduce el primer numero: ")))

	   op2=(float(input("Introduce el primer numero: ")))

	   print("La division es: " + str(op1/op2))

	except ValueError:
		print("El valor introducido no es correcto")

	except ZeroDivisionError:
		print("No se puede dividir entre cero")

	finally:	#Siempre se va a ejecutar lo que siga de este comando

	   print("Calculo finalizado")

divide()