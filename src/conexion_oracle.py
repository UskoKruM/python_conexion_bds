import cx_Oracle

"""
Si tienes problemas con tu base de datos en Oracle:

SQLPLUS / AS SYSDBA
Abrir conexión => ALTER PLUGGABLE DATABASE XEPDB1 OPEN;
"""

try:
    connection = cx_Oracle.connect(
        user='USUARIO',
        password='PASSWORD',
        dsn='localhost:1521/XEPDB2',  # Data Source Name
        encoding='UTF-8'
    )
    print(connection.version)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM NOMBRE_TABLA")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    connection.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado.")
