import pymysql

connection = pymysql.connect(host='localhost', port=3306
, user='getafe', password='mysql', database='HOSPITAL')
print("funciona????")

cursor= connection.cursor()
sql ="select * from EMP"
cursor.execute(sql)

for row in cursor:
    print(f"Apellido {row[1]}, oficio {row[2]}")

cursor.close()
connection.close()
print("Fin de programa")

