from services import service02prueba as service
#la otra forma de importar no me ha funcionado
#las clases van en el modelo
# y se ejecutan en el servicio donde está el método
from models import mascota
saludo = service.getSaludo()
print("Todo OK " + saludo)

pez = service.getMascota1()
leona = service.getMascota2()
print(pez.nombre)
print(leona.nombre)

