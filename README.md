# API Tester

API Tester es una herramienta diseñada para facilitar la prueba y validación de endpoints de diferentes APIs.

## Características

*   Pruebas de peticiones HTTP (GET, POST, PUT, DELETE, etc.).
*   Validación de respuestas y códigos de estado.
*   Almacenamiento de datos en SQLite.
*   Exportación de datos a CSV.
*   Menú interactivo para seleccionar opciones.
*   Fácil de configurar y extender.

## Tecnologías

*   Python
*   SQLite
*   Requests

## Instalación

Clona el repositorio e instala las dependencias:

```bash
git clone https://github.com/tu-usuario/api-tester.git
cd api-tester
pip install requests
```

Asegúrate de tener Python instalado.

## Uso

Ejecuta el programa:

```bash
python src/components/main.py
```

El programa presenta un menú interactivo con las siguientes opciones:

1.  **Obtener datos** - Solicita datos de una API y los guarda en SQLite.
2.  **Mostrar datos** - Muestra los datos almacenados en la base de datos.
3.  **Exportar datos** - Exporta los datos a un archivo CSV.
4.  **Eliminar datos** - Elimina los datos de la base de datos.
5.  **Salir** - Cierra la conexión y termina el programa.

## Contribución

¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.
