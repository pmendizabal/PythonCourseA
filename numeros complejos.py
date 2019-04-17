import cmath

print("Programa que calcula raiz cuadrada")
numero=int(input("Introduce un numero: "))


solucion=cmath.sqrt(numero)  #esto es un paquete
print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))