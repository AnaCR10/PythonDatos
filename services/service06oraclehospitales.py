import oracledb
from models import hospital as model

class ServiceOracleHospitales: 
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def getAllHospital(self):
        sql ="select * from HOSPITAL"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            hosp = model.Hospital() #creamos el objeto
            hosp.numero = row[0] #rellenamos el objeto datos filas
            hosp.nombre = row[1]
            hosp.direccion = row[2]
            hosp.telefono = row[3]
            hosp.num_cama = row[4]
            datos.append(hosp)# guardamos la información para mostrarla
        cursor.close()
        return datos
    
    def insertarHospital(self, numero, nombre, direccion, telefono, num_cama):
        sql = "insert into HOSPITAL values(:p1, :p2, :p3, :p4, :p5)"
        cursor = self.connection.cursor()
        cursor.execute(sql,(numero, nombre, direccion, telefono, num_cama))
        registro = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registro
    
    def eliminarHospitales (self, idhosp):
        sql = "delete from HOSPITAL where HOSPITAL_COD = :p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (idhosp,))
        registro = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registro
    
    def modificarHospitales (self,numero, nombre, direccion, telefono, num_cama):
        sql = "update HOSPITAL set nombre =:p1, direccion =:p2, telefono =:p3, num_cama =:p4 where HOSPITAL_COD=:p5"
        cursor = self.connection.cursor()
        cursor.execute(sql,(nombre, direccion, telefono, num_cama, numero))
        registro = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registro



