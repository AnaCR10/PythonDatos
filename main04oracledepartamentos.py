from services import service04oracledepartamento as service
from models import departamento

print (" --- SERVICIO ORACLE DEPARTAMENTOS ---")
#NECESITAMOS UN OBJETO DE TIPO SERVICIO PARA TRABAJAR, que se conecte a Oracle
servicio = service.ServiceOracleDepartamentos()

print("1. Inserte el departamento")
print("2. Buscar un departamento")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    print("Id de departamento: ")
    numero = int(input())
    print("Nombre del departamento: ")
    nombre = input()
    print("Localidad: ")
    localidad = input()
    #creamos una variable para que guarde cuando lo ejecutemos
    afectados = servicio.insertarDepartamento(numero,nombre,localidad)
    print(f" Departamentos insertados: {afectados}")
elif(opcion == 2):
    print("Buscador de departamento por ID")
    print("Introduzca el id del departamento")
    iddept = int(input())
    #declaramos una variable para guardar el departamento buscado
    dept = servicio.buscarDepartamentoId(iddept)
    print(f"el departamento es {dept.numero}, llamado {dept.nombre}, en {dept.localidad}")
    
print( " -- fin de programa -- ")


