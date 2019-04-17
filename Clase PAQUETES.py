"""
Los paquetes son directorios donde se almacenaran modulos
relacionados entre si.
Se crean mediante una carpeta con un archivo __init__.py

Ahora se crea la carpeta Calculos
Despues el archivo __init__ para dar cuenta que es un paquete
El archivo calculos_generales es un modulo

"""
#Lo primero es la carpeta paquete y despues el nombre del modulo
from Calculos.calculos_generales import dividir

dividir(4,2)

from Calculos.calculos_generales import potencia

potencia(2,4)

#De igual forma se pueden crear paquetes dentro de paquetes
#No olvides que deben llevar el archivo __init__ cada uno de estas carpetas paquete

from Calculos.basicos.operaciones_basicas import *

sumar(2,2)