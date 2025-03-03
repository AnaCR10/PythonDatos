import pymysql
from models.plantilla import Plantilla

class ServiceMySqlPlantilla: #se podría dejar ServiceEmpleados para no generar confusión
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', port=3306
        , user='getafe', password='mysql', database='HOSPITAL')

    def getPlantilla(self):
        sql= "select * from PLANTILLA"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data:list[Plantilla] = []
        for row in cursor:
            plant = Plantilla()
            plant.idPlantilla = row [2]
            plant.apellido = row[3]
            plant.funcion = row[4]
            plant.salario = row[6]
            plant.hospital = row[0]
            data.append(plant)
        cursor.close()
        return data
    def updateSalarioPlantilla(self, salario, hospital):
        sql = "update PLANTILLA set salario = salario + %s where HOSPITAL_COD= %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (salario, hospital))
        data:list[Plantilla] = []
        registro = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registro
   