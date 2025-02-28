import mysql.connector as bd
bd_conexion = bd.connect(host='localhost', port='3306', user='getafe', password='mysql', database='HOSPITAL')
cursor =bd_conexion.cursor()
print("Funciona????")

