from services import service08sqlserverplantilla as service
from models.plantilla import Plantilla

servicio = service.ServiceSQLServerPlantilla()



# from services import service08mysqlplantilla as service
# from models.plantilla import Plantilla

# servicio = service.ServiceMySqlPlantilla()



# from services import service08oracleplantilla as service
# from models.plantilla import Plantilla

# servicio = service.ServiceOraclePlantilla()

plantilla = servicio.getPlantilla()
for plant in plantilla:
    print("-------------------------------------------------------------------------")
    print (f"IdPlantilla: {plant.idPlantilla}  Apellido: {plant.apellido}, Función: {plant.funcion}, Salario: {plant.salario}, Hospital{plant.hospital}")
print("                        XXXXXXXXXXXX")
print("Introduzca el incremento a actualizar")
incremento = int(input())
print("Introduzca el hospital que quiere actualizar el salario")
hospital = int(input())
registro = servicio.updateSalarioPlantilla (incremento, hospital)
print (f"Plantilla modificada: {registro}")
print("                        XXXXXXXXXXXX")



