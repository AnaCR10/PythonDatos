import pyodbc
from models.plantilla import Plantilla

class ServiceSQLServerPlantilla:
    def __init__(self):
        self.connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=127.0.0.1;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')

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
        sql = "update PLANTILLA set salario = salario + ? where HOSPITAL_COD=?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (salario, hospital))
        data:list[Plantilla] = []
        registro = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registro
   