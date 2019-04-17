"""
Aqui haremos text y buttons, con text se introduce un texto
largo y con el buttons se usa para interactuar
"""

from tkinter import *

raiz= Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar() #Esto solo para ejemplificar el funcionamiento de Button

#Con grid() podemos poner una cuadricula y asi ubicar mejor los widgets que queramos
cuadroNombre=Entry(miFrame, textvariable=minombre)
#cuadroTexto.place(x=100,y=100) Esto ya no lo necesitamos ya que:
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center") #De aqui manipulamos el color de las letras, el estilo, forma, etc

#Aqui se genera el widget de password y a continuacion en config, al poner show hacemos que solo se vea los *
cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)



textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew") #con sticky se adapta el scroll

textoComentario.config(yscrollcommand=scrollVert.set) #ahora el indicador de scroll se adapta

nombreLabel=Label(miFrame, text="Nombre:")
#nombreLabel.place(x=100, y=100) #Con esto, solo empujas al otro widget
nombreLabel.grid(row=0, column=0, sticky="w") #Con sticky podemos localizar el texto donde queramos

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="w")

DireccionLabel=Label(miFrame, text="Direccion:")
DireccionLabel.grid(row=3, column=0)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

#Tambien existe pad que permite ubicar entre widgets, por ejemplo
#si pongo padx=150, esto hara que el widget se coloque a 150 pixeles del otro widget sobre el eje x

def codigoBoton():

	minombre.set("Juan")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
#Con el argumento command podemos hacer que el boton desencadene distintas acciones
botonEnvio.pack()

raiz.mainloop()