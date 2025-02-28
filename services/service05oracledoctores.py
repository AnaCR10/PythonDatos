import oracledb
from models import doctor as model #le damos un alias para separa el fichero de lo que queremos

class ServiceOracleDoctores: #creamos la clase
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def getAllDoctores(self):
        sql = "select * from DOCTOR"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            doc = model.Doctor() #creamos un objeto
            doc.idDoctor = row[1] #rellenamos las filas del objeto
            doc.apellido = row[2]
            doc.especialidad = row[3]
            doc.salario = row[4]
            doc.hospital = row[0]
            datos.append(doc)# aquí añadimos cada doctor a la lista
        cursor.close()
        return datos
    
    def insertarDoctor(self, hospital, iddoctor,apellido, especialidad, salario ):
        sql = "insert into DOCTOR values(:p1, :p2, :p3, :p4, :p5) "
        cursor = self.connection.cursor()
        cursor.execute(sql,(hospital,iddoctor, apellido, especialidad, salario ))
        registro = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registro
    
    def modificarDoctor(self,hospital,apellido, especialidad, salario, iddoctor ):
        sql ="update DOCTOR set hospital_cod=:p1, apellido=:p2, especialidad=:p3, salario=:p4 where DOCTOR_NO=:p5"
        cursor =self.connection.cursor()
        cursor.execute(sql,(hospital,apellido, especialidad, salario, iddoctor))
        registro = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registro
    
    def eliminarDoctor(self, iddoctor):
        sql ="delete from DOCTOR where DOCTOR_NO = :p1"
        cursor = self.connection.cursor()
        cursor.execute(sql,(iddoctor,))
        registro = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registro
    


    
    



        





