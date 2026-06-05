import requests
import sqlite3

global datos
ruta_db = "src/database/database.db"
conn = sqlite3.connect(ruta_db) # conectamos con la base de datos
sql = conn.cursor() # creamos un cursor para ejecutar comandos SQL

def fetch(url):
    global datos
    try: # pedimos los datos a la url
        respuesta = requests.get(url)
        datos = respuesta.json()
    except(FileNotFoundError):
        print("Url no disponible")
    
    print(datos)

# api web del tiempo: fetch("https://api.open-meteo.com/v1/forecast?latitude=40.4168&longitude=-3.7038&current=temperature_2m")