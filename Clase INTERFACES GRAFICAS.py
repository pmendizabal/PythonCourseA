"""
Tambien denominadas GUI, son intermediarios entre el programa y el usuario.
Formadas por un conjunto de graficos como botones, ventanas, etc.
Libreria:
Tkinter
WxPython
PyQT
PyGTK

Estructura de ventana con Tkinter

Raiz(tk)
 Frame que corresponde a aglutinar elementos
   widgets que son botones, ventanitas, etc

"""

from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(0,0) #aqui para permitir ajustes a la ventana (ancho y alto), esto es booleano

#Para cambiar el icono de la ventana, se debe tener un archivo .ico para cargarlo
#raiz.iconbitmap("gato.ico") #esto es la manera de introducir esto

#Para cambiar tamaño de la ventana
#raiz.geometry("650x350")

#Para cambiar el color de fondo
raiz.config(bg="blue")

#Para que no se abra la consola y solo la ventana, hay que cambiar la extension del archivo del programa a .pyw

miFrame=Frame()

miFrame.pack(side="left", anchor="n") #Con esto el frame ya esta en la raiz que es algo necesario. Tambien puedes dominar la posicion del frame en la raiz utilizando los argumentos señalados

#miFrame.pack(fill="y",expand="True") #Con esto, el frame se adapta en el eje Y a la raiz
#miFrame.pack(fill="both", expand="True") #Y con esto, se adapta en todo el frame con la raiz

miFrame.config(bg="red")

miFrame.config(width="650", height="350") #la raiz se adapta al frame pero la raiz tiene otro tamaño

miFrame.config(bd=35) #Cambia el grosor del frame

miFrame.config(relief="groove")

miFrame.config(cursor="hand2")

raiz.mainloop() #mainloop es un bucle infinito, aqui una ventana debe estar en continuo funcionamiento
#mainloop siempre debe estar al final

#Todo lo aplicado al frame se puede aplicar a la raiz, todo depende de lo que se quiera