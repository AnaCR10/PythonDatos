from models import persona

def getPersona():
    dato = persona.Persona()#creamos un objeto de la clase persona
    dato.nombre = "Amparo"
    dato.edad = 30
    dato.email = "amparo@gmail.com"
    return dato

