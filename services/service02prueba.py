from models import mascota
def getSaludo():
    return "Bienvenido a SQL Server"


def getMascota1():
    dato = mascota.Mascota()
    dato.nombre = "Patricio"
    dato.raza = "Estrella de mar"
    dato.edad = 8
    return dato

def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Sebastian"
    dato.raza = "Cangrejo"
    dato.edad = 9
    return dato