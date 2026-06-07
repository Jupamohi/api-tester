import csv

import requests
import sqlite3

global datos
ruta_db = "src/database/database.db"
conn = sqlite3.connect(ruta_db) # conectamos con la base de datos
sql = conn.cursor() # creamos un cursor para ejecutar comandos SQL

# función para obtener los datos de una url y guardarlos en la variable global "datos"
def fetch(url):
    global datos
    try: # pedimos los datos a la url
        respuesta = requests.get(url)
        datos = respuesta.json()
        sql.execute("""
    CREATE TABLE IF NOT EXISTS datos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userId INTEGER, 
        post_id INTEGER,
        title TEXT, 
        body TEXT
    )
                    """) # creamos la tabla "datos" si no existe
        sql.execute(
    "INSERT OR IGNORE INTO datos (userId, post_id, title, body) VALUES (?, ?, ?, ?)", 
    (datos['userId'], datos['id'], datos['title'], datos['body'])
                    ) # insertamos los datos en la tabla
        conn.commit() # guardamos los cambios en la base de datos
    except(requests.exceptions.RequestException) as e:
        print("Url no disponible")
        print(e)

    print(datos)

# función para mostrar los datos obtenidos
def stats():
    # Obtenemos los datos y usamos fetchall() para ver las filas
    cursor = conn.execute("SELECT * FROM datos")
    rows = cursor.fetchall()
    if rows:
        print("Datos obtenidos:")
        for row in rows:
            print("\n",row)
    else:
        print("No se han obtenido datos aún.")


def export():
    try:
        cursor = conn.execute("SELECT * FROM datos")
        rows = cursor.fetchall()
        
        if not rows:
            print("No hay datos para exportar.")
            return
        
        with open("datos.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "userId", "post_id", "title", "body"])  # headers
            writer.writerows(rows)
        
        print(f"✓ {len(rows)} registros exportados a datos.csv")
    except Exception as e:
        print(f"Error al exportar: {e}")
def eliminar():
    global datos
    sql.execute("DELETE FROM datos") # eliminamos los datos de la base de datos
    conn.commit() # guardamos los cambios en la base de datos
    print("Datos eliminados")


while True:
    print("1. Obtener datos")
    print("2. Mostrar datos")
    print("3. Exportar datos")
    print("4. Eliminar datos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            # url = input("Ingrese la URL: ")
            fetch("https://jsonplaceholder.typicode.com/posts/1")
        case "2":
            stats()
        case "3":
            export()
        case "4":
            eliminar()
        case "5":
            conn.close() # cerramos la conexión con la base de datos
            break
        case _:
            print("Opción no válida")



# Ejemplos de APIs públicas (sin autenticación):

# JSONPlaceholder → datos fake de posts, usuarios, comentarios
# GET https://jsonplaceholder.typicode.com/posts
# Open-Meteo → clima/meteorología
# GET https://api.open-meteo.com/v1/forecast?latitude=40.4168&longitude=-3.7038&current=temperature_2m
# Random User Generator → usuarios fake
# GET https://randomuser.me/api/?results=10