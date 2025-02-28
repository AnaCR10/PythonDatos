import oracledb
from models import departamento

class ServiceOracleDepartamentos:
   # va a tener una conexión
   def __init__(self):
      #creamos un objeto connection
      self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

   def insertarDepartamento(self,numero, nombre, localidad):
      sql = "insert into DEPT values( :id, :nombre, :localidad)"
      cursor = self.connection.cursor()
      cursor.execute(sql,(numero, nombre, localidad))
      registro = cursor.rowcount # nos guardamos los datos, es opcional
      self.connection.commit() #esto hace que se guarden los datos de forma permanente
      cursor.close()
      return registro
   #en este caso no hace falta cerrar la conexión, al estar en la clase se destruye.

   def buscarDepartamentoId(self,numero):
      sql = "select * from DEPT where DEPT_NO = :p1"
      cursor = self.connection.cursor()
      cursor.execute(sql,(numero,))
      row = cursor.fetchone()# con esto nos traemos el dato
      #creamos nuestro departamento modelo
      modelo = departamento.Departamento()
      #asignamos los datos del row al modelo
      modelo.numero = row[0] #primera fila de la tabla
      modelo.nombre = row[1] #segunda fila
      modelo.localidad = row[2] #tercera fila
      cursor.close()
      return modelo

   def borrarDepartamento(self,numero):
      sql = "delete from DEPT where DEPT_NO = :p1"
      cursor= self.connection.cursor()
      cursor.execute(sql,(numero,))
      registro = cursor.rowcount
      self.connection.commit()
      cursor.close()
      return registro
   

   def modificarDepartamento(self, numero, nombre, localidad):
      sql = "update DEPT set DNOMBRE=:p1, LOC=:p2 where DEPT_NO=:p3"
      cursor=self.connection.cursor()
      cursor.execute(sql,(nombre, localidad, numero))
      registro = cursor.rowcount
      self.connection.commit()
      cursor.close() 
      return registro
    
   def getAllDepartamentos(self):
      sql = "select * from DEPT"
      cursor = self.connection.cursor()
      cursor.execute(sql)
      #creamos una lista para almacenar cada departamento
      datos = []
      #recorremos el cursor de datos
      for row in cursor:
         #por cada vuelta de bucle hay que crear un nuevo objeto, en este caso departamento
         dept = departamento.Departamento()
         dept.numero = row[0]
         dept.nombre = row [1]
         dept.localidad = row [2]
         datos.append(dept) #aquí almaceno todos los datos del objeto departamento
      cursor.close()
      return datos
