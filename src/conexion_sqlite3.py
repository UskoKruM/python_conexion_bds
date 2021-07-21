import sqlite3

try:
    """
    mi_conexion = sqlite3.connect("database/miprimerabd")
    cursor = mi_conexion.cursor()
    cursor.execute("CREATE TABLE persona (nombre VARCHAR(50), edad INTEGER)")
    """
    mi_conexion = sqlite3.connect("database/Universidad.sqlite3")
    cursor = mi_conexion.cursor()
    cursor.execute("SELECT * FROM Academico_curso")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
