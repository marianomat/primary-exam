import sqlite3
import sql.seeds as seeds

# Creamos la conexión con la DB, si no existe la crea
conn = sqlite3.connect("aeropuerto3.db")

# Creamos el objeto cursor
cursor = conn.cursor()

# Creamos el esquema
try:
    print("Creando la tabla Empleado")
    cursor.execute("CREATE TABLE IF NOT EXISTS empleado (eid INTEGER PRIMARY KEY, enombre TEXT, sueldo REAL);")
    print("Creando la tabla Aeronave")
    cursor.execute("CREATE TABLE IF NOT EXISTS aeronave (aid INTEGER PRIMARY KEY, anombre TEXT, rango INTEGER);")
    print("Creando la tabla Certificado")
    cursor.execute("CREATE TABLE IF NOT EXISTS certificado (eid INTEGER REFERENCES empleado(eid), aid INTEGER "
                   "REFERENCES "
                   "aeronave(aid), "
                   "PRIMARY KEY (eid, aid));")
    print("Creando la tabla Vuelo")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS vuelo (vuelonro INTEGER PRIMARY KEY, desde TEXT, hacia TEXT, distancia TEXT, partida TEXT, "
        "arribo TEXT, precio REAL);")
except:
    print("Error creando las tablas")

## Populate DB con seeds
try:
    # Empleados
    insert_query = "INSERT INTO empleado (enombre, sueldo) VALUES(?, ?)"
    cursor.executemany(insert_query, seeds.get_personas())

    # Aeronaves
    insert_query = "INSERT INTO aeronave (anombre, rango) VALUES(?, ?)"
    cursor.executemany(insert_query, seeds.get_aeronaves())

    # Vuelos
    insert_query = "INSERT INTO vuelo (desde, hacia, distancia, partida, arribo, precio) VALUES(?,?,?,?,?,?)"
    cursor.executemany(insert_query, seeds.get_vuelos())

    # Certificados
    insert_query = "INSERT INTO certificado (eid, aid) VALUES(?, ?)"
    cursor.executemany(insert_query, seeds.get_relacion_persona_aeronave())
except:
    print("Error populando la DB")

# Select
# Select de empleados pilotos
pilotos = cursor.execute(
    "SELECT empleado.enombre, a.anombre FROM empleado "
    "INNER JOIN certificado ON empleado.eid = certificado.eid "
    "INNER JOIN aeronave a on certificado.aid = a.aid")

print("Pilotos:")
print(pilotos.fetchall())

# Update: cambiar precio del vuelo 1
cursor.execute("UPDATE vuelo SET precio = 4000 WHERE vuelonro = 1")

# Delete eliminar vuelo 2
cursor.execute("DELETE FROM vuelo WHERE vuelonro = 2")

# Parte 2: consulta
# “Listar los nombres de los pilotos que pueden volar aeronaves con rango de crucero
# mayor a 5000 millas pero que SOLO está certificado con aviones Boeing (es decir si
# esta certificado en Boeing y otro tipo de avión no debe estar incluido en el resultado)”

query = cursor.execute(
    "SELECT enombre FROM empleado INNER JOIN certificado c2 on empleado.eid = c2.eid WHERE empleado.eid NOT IN (SELECT e.eid as rango FROM empleado e INNER JOIN certificado c on e.eid = c.eid INNER JOIN aeronave a on a.aid = c.aid WHERE a.rango < 5000 and a.anombre NOT LIKE '%Boeing%')")

print("Respuesta query")
print("El unico empleado que cumple la condicion es el (eid=3, aid=3) Carrie Wood")
print(query.fetchall())
conn.commit()

# Cerramos la conexion
conn.close()
