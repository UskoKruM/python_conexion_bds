import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=USKOKRUM2010;DATABASE=django_api;UID=sa;PWD=123456')
    # connection = pyodbc.connect('DRIVER={SQL Server};SERVER=USKOKRUM2010;DATABASE=django_api;Trusted_Connection=yes;')
    print("Conexión exitosa.")
    cursor = connection.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    print("Versión del servidor de SQL Server: {}".format(row))
    cursor.execute("SELECT * FROM tarea")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    connection.close()  # Se cerró la conexión a la BD.
    print("La conexión ha finalizado.")
