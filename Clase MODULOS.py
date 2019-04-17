"""
Modulos

Son archivos con extension .py o .pyc o un archivo escrito en C
paraa CPython, que posee su propio espacio de nombres y que puede
contener variables, funciones, clases e incluso otros modulos.
Sirven para modularizacion y reutilizacion de codigo.
Recuerda que la modularizacion se refiere a fraccionar el programa
para volverlo comprensible.

"""
import sys #Linea 12 y 13 para localizar el modulo en la pc
sys.path.insert(0, '/Users/Thosiba User/Documents/PYTHON/Modulos')

"""
import funciones_matematicas_ClaseModulos

funciones_matematicas_ClaseModulos.sumar(2,2)

funciones_matematicas_ClaseModulos.restar(2,2)

funciones_matematicas_ClaseModulos.multiplicar(2,2)

#Pero es muy engorroso todo esto, entonces podemos usar
"""

from funciones_matematicas_ClaseModulos import * #Con el * indicamos que queremos todas las funciones del modulo

sumar(2,2)

resta(5,3)

multiplicar(3,3)

#Recuerda que python importa el modulo desde la misma carpeta donde esta el programa que lo llama
# si no lo encuentra, entonces se va al syspath
