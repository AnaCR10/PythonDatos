from services import service05oracledoctores as service
from models import doctor as model

print(" --- ESTO ES UN CRUD DE DOCTORES ---")
servicio = service.ServiceOracleDoctores() #creamos nuestra variable servicio 
doctores = servicio.getAllDoctores()
for doc in doctores:
    print(f"Apellido {doc.apellido}, Especialidad {doc.especialidad}, Salario {doc.salario}")
print(" --- FIN DE PROGRAMA ---")

print("1. Inserte un doctor")
print("2. Eliminar doctor de la bbdd")
print("3. Modificar ficha de un doctor")
print("4. --------------")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    print("ID del doctor")
    iddoctor = input()
    print("Apellido")
    apellido = input()
    print ("Especialidad")
    especialidad = input()
    print("Salario")
    salario= int(input())
    print("Código de Hospital")
    hospital = int(input())
    registros = servicio.insertarDoctor(hospital,iddoctor, apellido, especialidad, salario)
    print(f"Doctores insertados : {registros}")
elif (opcion == 2):
    print("Dame el ID del doctor a eliminar de la bbdd")
    iddoctor = int(input())
    registros =servicio.eliminarDoctor(iddoctor)
    print(f"Nº de Doctores eliminados: {registros}")
elif (opcion == 3):
    print("Dame el ID del doctor que quieras modificar")
    iddoctor = int(input())
    #,hospital,apellido, especialidad, salario, iddoctor 
    print("Dame el código del hospital")
    hospital = int(input())
    print("Dame el apellido del doctor")
    apellido= input()
    print("Dame la especialidad")
    especialidad= input()
    print("Dame el nuevo salario")
    salario= int(input())
    registros = servicio.modificarDoctor(hospital,apellido, especialidad, salario, iddoctor)
    print(f"Se ha modificado {registros} doctor ")

    


print("Fin de programa")
