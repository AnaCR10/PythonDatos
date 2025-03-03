import oracledb
from models.plantilla import Plantilla

class ServiceOraclePlantilla:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

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
        sql = "update PLANTILLA set salario = salario + :p1 where HOSPITAL_COD=:p2"
        cursor = self.connection.cursor()
        cursor.execute(sql, (salario, hospital))
        data:list[Plantilla] = []
        registro = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registro
    



