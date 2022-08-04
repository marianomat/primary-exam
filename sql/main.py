import sqlite3

# Creamos la conexión con la DB, si no existe la crea
import sql.seeds as seeds

conn = sqlite3.connect("aeropuerto2.db")

# Creamos el objeto cursor
cursor = conn.cursor()

# Creamos el esquema
try:
    print("Creando la tabla Empleado")
    cursor.execute("CREATE TABLE IF NOT EXISTS empleado (eid INTEGER PRIMARY KEY, enombre TEXT, sueldo REAL);")
    print("Creando la tabla Aeronave")
    cursor.execute("CREATE TABLE IF NOT EXISTS aeronave (aid INTEGER PRIMARY KEY, anombre TEXT, rango TEXT);")
    print("Creando la tabla Certificado")
    cursor.execute("CREATE TABLE IF NOT EXISTS certificado (eid INTEGER REFERENCES empleado(eid), aid INTEGER REFERENCES "
                   "aeronave(aid), "
                   "PRIMARY KEY (eid, aid));")
    print("Creando la tabla Vuelo")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS vuelo (vuelonro INTEGER PRIMARY KEY, desde TEXT, hacia TEXT, distancia TEXT, partida TEXT, "
        "arribo TEXT, precio REAL);")
except:
    print("Error creando las tablas")

insert_query = "insert into empleado (enombre, sueldo) values(?, ?)"

cursor.executemany(insert_query, seeds.get_personas())

conn.commit()

# Cerramos la conexion
conn.close()
