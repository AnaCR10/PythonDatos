import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=127.0.0.1;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')
print("Funciona SQL Server")

sql = "select * from EMP where SALARIO>= ?"
cursor = connection.cursor()
print("Introduzca un salario")
salario = int(input())
cursor.execute(sql, (salario,))
for row in cursor:
    print(f"Apellido {row[1]}, Oficio: {row[2]}, Salario: {row[5]}")
cursor.close()
connection.close()
print("Fin de programa")