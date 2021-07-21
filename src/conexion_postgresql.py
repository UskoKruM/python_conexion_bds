import psycopg2
from psycopg2 import DatabaseError

try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456',
        database='universidad'
    )

    print("Conexión exitosa.")
    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print("Versión del servidor de PostgreSQL: {}".format(row))
    cursor.execute("SELECT * FROM curso")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except DatabaseError as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    connection.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado.")
