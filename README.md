# API Tester

API Tester es una herramienta diseñada para facilitar la prueba y validación de endpoints de diferentes APIs.

> **Nota importante**: Si bien el proyecto se llama "API Tester", actualmente no puede probar cualquier API de forma genérica. Esto se debe a que cada API devuelve datos en formatos diferentes y el código actualmente está diseñado para manejar una estructura específica de datos (compatible con JSONPlaceholder). Para que el proyecto pueda adaptarse a diferentes APIs, sería necesario implementar un sistema dinámico que permita configurar o inferir la estructura de datos que devuelve cada API. Esta funcionalidad está planeada para futuras releases.

## Características

*   Pruebas de peticiones HTTP (GET, POST, PUT, DELETE, etc.).
*   Validación de respuestas y códigos de estado.
*   Almacenamiento de datos en SQLite.
*   Exportación de datos a CSV.
*   Estadísticas de posts por usuario.
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

1.  **Obtener datos** - Solicita datos de una API (actualmente configurada para JSONPlaceholder) y los guarda en SQLite.
2.  **Mostrar datos** - Muestra estadísticas de los datos almacenados (total de posts y posts por usuario).
3.  **Exportar datos** - Exporta los datos a un archivo CSV.
4.  **Eliminar datos** - Elimina los datos de la base de datos.
5.  **Salir** - Cierra la conexión y termina el programa.

## Funciones

*   `fetch(url)` - Realiza una petición GET a la URL proporcionada, guarda la respuesta JSON en la variable global `datos` y la almacena en la base de datos SQLite.
*   `stats()` - Muestra estadísticas de los datos almacenados: total de posts y distribución de posts por usuario.
*   `export()` - Exporta todos los registros de la base de datos a un archivo CSV llamado `datos.csv`.
*   `eliminar()` - Elimina todos los datos de la tabla `datos` en la base de datos.

## Estructura de la base de datos

La tabla `datos` tiene la siguiente estructura:

| Campo   | Tipo    | Descripción            |
|---------|---------|------------------------|
| id      | INTEGER | Clave primaria         |
| userId  | INTEGER | ID del usuario         |
| post_id | INTEGER | ID del post            |
| title   | TEXT    | Título del post        |
| body    | TEXT    | Contenido del post     |

## APIs compatibles (actualmente)

El código está diseñado para trabajar con APIs que devuelvan una estructura similar a JSONPlaceholder:

*   JSONPlaceholder: `https://jsonplaceholder.typicode.com/posts/{id}`

## Contribución

¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.