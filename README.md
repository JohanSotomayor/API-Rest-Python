# Sales Management System

Este proyecto es una API RESTful de backend para un sistema de administración de ventas creado con Flask y SQLAlchemy.

## Descripción

La API RESTful del sistema de administración de ventas permite gestionar clientes, productos y ventas. Incluye funcionalidades para crear, leer, actualizar y eliminar (CRUD) datos en la base de datos.

## Requisitos

- Python 3.x
- Flask
- Flask-SQLAlchemy
- PyODBC (para conectar a SQL Server)
- dotenv (para gestión de variables de entorno)

## Configuración de CORS

El proyecto utiliza CORS (Cross-Origin Resource Sharing) para permitir el acceso desde diferentes orígenes. Se ha configurado CORS con un prefijo de API para asegurar que solo las rutas bajo `/api` puedan ser accedidas desde cualquier origen.

La configuración de CORS se ve así:

- Prefijo de API: `/api`
- Orígenes Permitidos: `*` (cualquier origen)

Esto significa que cualquier solicitud realizada a las rutas bajo `/api` desde cualquier origen será permitida.

## Instalación

1. Clona el repositorio:

   git clone https://github.com/JohanSotomayor/API-Rest-Python.git
   
2. Crea y activa un entorno virtual:

    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

3. Instala las dependencias:

    pip install -r requirements.txt

4. Crea un archivo .env en el directorio raíz del proyecto y agrega tus variables de entorno:

    DB_HOST
    DB_PORT
    DB_USER
    DB_PASSWORD
    DB_NAME

5. Ejecuta la aplicación:

    python main.py



## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.
