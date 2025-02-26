#tengo que llamar a mascota para poder ejecutar el método de mascota
#import models.mascota este no funciona
from models import mascota

#este servicio será el que tendrá métodos para ser utilizados en el main
def getSaludo():
    return "Bienvenido a Matrix"


def getMascota1():
    dato = mascota.Mascota()
    dato.nombre = "Flounder"
    dato.raza = "Pez"
    dato.edad = 22
    return dato

def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Nala"
    dato.raza = "Leona"
    dato.edad = 17
    return dato
