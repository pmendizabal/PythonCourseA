"""
En esta clase se realizara un widget para introducir texto
"""

from tkinter import *

raiz= Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#Con grid() podemos poner una cuadricula y asi ubicar mejor los widgets que queramos
cuadroNombre=Entry(miFrame)
#cuadroTexto.place(x=100,y=100) Esto ya no lo necesitamos ya que:
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="red", justify="center") #De aqui manipulamos el color de las letras, el estilo, forma, etc

#Aqui se genera el widget de password y a continuacion en config, al poner show hacemos que solo se vea los *
cuadroPass=Entry(miFrame)
cuadroPass.grid()
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1)


nombreLabel=Label(miFrame, text="Nombre:")
#nombreLabel.place(x=100, y=100) #Con esto, solo empujas al otro widget
nombreLabel.grid(row=0, column=0, sticky="w") #Con sticky podemos localizar el texto donde queramos

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="w")

DireccionLabel=Label(miFrame, text="Direccion de casa:")
DireccionLabel.grid(row=2, column=0)

#Tambien existe pad que permite ubicar entre widgets, por ejemplo
#si pongo padx=150, esto hara que el widget se coloque a 150 pixeles del otro widget sobre el eje x


raiz.mainloop()