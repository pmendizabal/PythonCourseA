from tkinter import *
"""
Esta es una forma para que tkinter funcione con png o jpg, recuerda que 
se debe actualizar en esta compu

from PIL import Image, ImageTk

self.img1 = Image.open("AW1.png")
self.pic1 = ImageTk.PhotoImage(self.img1)
"""

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montaña=IntVar()
turismoRural=IntVar()

def opcionesViaje():

	opcionEscogida=""

	if(playa.get()==1):
		opcionEscogida+=" playa"

	if(montaña.get()==1):
		opcionEscogida+=" montaña"

	if(turismoRural.get()==1):
		opcionEscogida+=" turismo rural"

	textoFinal.config(text=opcionEscogida)


foto=PhotoImage(file="AW.gif")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montaña, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()



root.mainloop()