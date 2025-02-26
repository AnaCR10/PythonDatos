from services import service03personas as service
from models import persona
print(" --- MAIN DE PERSONAS ---")
mujer = service.getPersona()
print(f"Esta persona se llama: {mujer.nombre}, tiene {mujer.edad} años y su mail es {mujer.email}" )
print(" -- fin de programa --")