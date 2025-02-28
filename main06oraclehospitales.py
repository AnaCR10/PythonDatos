from services import service06oraclehospitales as service
from models import hospital as model

print("----   CRUD DE HOSPITALES   ----")
servicio= service.ServiceOracleHospitales() #nuestra variable de servicio
print("0. Mostrar todos los hospitales")
print("1. Inserte un Hospital")
print("2. Eliminar Hospital de la bbdd")
print("3. Modificar ficha de un hospital")
opcion = int(input())
if (opcion == 0):
    
    hospitales = servicio.getAllHospital()
    for hosp in hospitales:
        print(f"Número {hosp.numero}, Nombre{hosp.nombre}, Dirección {hosp.direccion}, Teléfono {hosp.telefono}, N de cama {hosp.num_cama}")  

elif (opcion == 1): #insertar
    print("Código de Hospital")
    idhosp = int(input())
    print("Nombre: ")
    nombre = input()
    print("Dirección: ")
    direccion = input()
    print("Teléfono: ")
    telefono = input()
    print("Número de camas: ")
    num_camas = int(input())
    registro = servicio.insertarHospital(idhosp,nombre,direccion, telefono, num_camas)
    print (f"Hospitales insertados: {registro}")
elif (opcion == 2): #eliminar
    print("Dame el código del Hospital a eliminar de la BBDD")
    idhosp = int(input())
    registro = servicio.eliminarHospitales(idhosp)
    print(f"Hospitales eliminados: {registro}")
elif (opcion == 3): #modificar
    print("Código de Hospital:")
    idhosp = int(input())
    print("Nombre:")
    nombre = input()
    print("Dirección:")
    direccion = input()
    print("Teléfono:")
    telefono = input()
    print("Número de camas:")
    num_camas = int(input())
    registro = servicio.modificarHospitales(idhosp, nombre, direccion, telefono,num_camas)
    print (f"Hospitales modificados: {registro}")

print("  ---- FIN DE PROGRAMA ----")





