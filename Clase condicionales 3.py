"""edad=7

if 0<edad<100:
	print("Edad es correcta")
else:
	print("Edad incorrecta") """


salario_presidente=int(input("Introduce el salario del presidente: "))
print("Salario del presidente: " + str(salario_presidente))

salario_director=int(input("Introduce el salario del director: "))
print("Salario del director: " + str(salario_director))

salario_jefe=int(input("Introduce el salario del jefe: "))
print("Salario del jefe: " + str(salario_jefe))

salario_proletariado=int(input("Introduce el salario del proletariado: "))
print("Salario del proletariado: " + str(salario_proletariado))

if salario_presidente>salario_director>salario_jefe>salario_proletariado:
	print("El capitalismo funciona")
else:
	print("Una anomalía se ha detectado")