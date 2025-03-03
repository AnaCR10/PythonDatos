import oracledb
from models.empleado import Empleado

class ServiceOracleEmpleados:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def getEmpleados(self):
        sql = "select * from EMP"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        #aquí debemos indicar el tipo de lista que estamos devolviendo
        #para hacerlo:
        # variable:list[tipo de clase]= []
        data:list[Empleado] = []
        for row in cursor:
            emp = Empleado() #llamamos a la clase Empleado, objeto, para darle los datos
            emp.idEmpleado = row [0]
            emp.apellido = row[1]
            emp.oficio = row[2]
            emp.salario = row[5]
            data.append(emp) #guardamos la info en nuestra lista
        cursor.close()
        return data
    
    def getEmpleadosSalario(self,salario):
        sql = "select * from EMP where SALARIO >= :p1"
        cursor = self.connection.cursor()
        cursor.execute(sql,(salario,))
        data:list[Empleado] = [] #así sabe que es un objeto de Empleado, está tipado como Empleado
        for row in cursor:
            emp = Empleado() #llamamos a la clase Empleado, objeto, para darle los datos
            emp.idEmpleado = row [0]
            emp.apellido = row[1]
            emp.oficio = row[2]
            emp.salario = row[5]
            data.append(emp) #guardamos la info en nuestra lista
        cursor.close()
        return data

 
    

    