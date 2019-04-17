"""
Con los Labels permiten mostrar texto o imagenes.
La sintaxis es:
varLabel=Label(contenedor,opciones)
"""

from tkinter import *

root=Tk()

miFrame=Frame(root,width=500,height=400)

miFrame.pack()

miImagen=PhotoImage(file="AW.gif", format="gif -index2")

"""
miLabel=Label(miFrame, text="Hola mundo")
miLabel.place(x=100,y=200) #Permite ubicar el texto en cualquier espacio
"""

#Esto con una imagen
Label(miFrame, image=miImagen).place(x=100,y=200)

#Esto con texto
#Label(miFrame, text="Hola mundo", fg="red", font=("Times New Warren",18)).place(x=100,y=200)

root.mainloop()