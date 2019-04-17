# coding=utf-8﻿ 

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):   #Aqui viene un posible error, agregamos excepcion para que el programa no se rompa aqui

	try:	
	  return num1/num2
	
	except ZeroDivisionError:  #Hay que describir el error explicitamente
		print("No se puede dividir entre cero")
		return "Operacion erronea"


while True:  #con este bucle podemos volver a pedir los numeros si se introducen letras
  try:
      op1=(int(input("Introduce el primer numero: ")))

      op2=(int(input("Introduce el segundo numero: ")))	

      break	

  except ValueError:
	   print("No se esta introduciendo numeros")
	
operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")