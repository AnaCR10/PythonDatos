from services import service07sqlserverempleados as service
from models.empleado import Empleado

print("Probando servicios varios de BBDD")
#primero creamos el de Oracle/MySQL/SQLServer lo que queramos
servicio = service.ServiceSQLServerEmpleados()

empleados = servicio.getEmpleados()
for emp in empleados:
    print (f"Apellido: {emp.apellido}, Oficio: {emp.oficio}, Salario: {emp.salario}")

print("Introduzca un salario para buscar")
salario = int(input())
empleados = servicio.getEmpleadosSalario(salario)
for emp in empleados:
    print (f"Apellido: {emp.apellido}, Oficio: {emp.oficio}, Salario: {emp.salario}")
print("Fin de programa")
