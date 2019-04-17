"""
El proposito es guardar datos de forma permanente en ficheros

Para recordar y repasar:
VIDEO 41 DE PILDORASINFORMATICAS CURSO DE PYTHON
"""

import pickle

class Persona:

    def __init__(self, nombre, genero, edad):

        self.nombre=nombre
        self.genero=genero
        self.edad=edad

        print("Se ha creado una persona nueva llamada: ", self.nombre)

    def __str__(self):

        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:

    personas=[]

    def __init__(self):

        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0) #Esto para poner el curso siempre al comienzo y poder agregar nuevas personas

        try:

            self.personas=pickle.load(listaDePersonas)
            print("Se ha cargado {} personas del fichero externo".format(len(self.personas)))

        except:

            print("El fichero esta vacio")

        finally:

            listaDePersonas.close()
            del (listaDePersonas)

    def agregarPersonas(self, p):

        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:

            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)

    def mostrarInfoFicheroExterno(self):

        print("La informacion del fichero externo es ")
        for p in self.personas:
            print(p)


miLista=ListaPersonas()

persona=Persona("Juan", "Hombre", "26") #De aqui ponemos agregar info y no se borra

miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()


