from services import service04oracledepartamento as service
from models import departamento

print (" --- SERVICIO ORACLE DEPARTAMENTOS ---")
#NECESITAMOS UN OBJETO DE TIPO SERVICIO PARA TRABAJAR, que se conecte a Oracle
servicio = service.ServiceOracleDepartamentos()

print(" ------- DEPARTAMENTOS -------")
datos = servicio.getAllDepartamentos()
for dept in datos:
    print(f" {dept.numero}, {dept.nombre}, {dept.localidad}")
print (" ---------- ")
print("1. Inserte el departamento")
print("2. Buscar un departamento")
print("3. Borrar el departamento")
print("4. Modificar un departamento")
#print("5. Mostrar todos los departamentos")
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
elif (opcion == 3):
    print("Introduzca el departamento que desea borrar")
    deptBorrar = int(input())
    borrado = servicio.borrarDepartamento(deptBorrar)
    print(f"Hemos borrado {borrado} departamento")
elif (opcion == 4):
    print("----Modificar departamento----")
    print("Introduzca el ID del departamento")
    iddept = int(input())
    print("Nuevo nombre de departamento")
    nombre = input()
    print("Localidad:")
    localidad = input()
    registros = servicio.modificarDepartamento(iddept, nombre, localidad)
    print(f"Departamentos modificados: {registros}")
#elif (opcion == 5):
    

    
print( " -- fin de programa -- ")


