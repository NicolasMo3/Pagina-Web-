Australens CRM - Gestión de Clientes
Australens CRM es una aplicación web diseñada para facilitar la gestión de clientes en una empresa. Desarrollada con Django, esta herramienta permite almacenar, organizar y acceder a información de clientes, simplificando el seguimiento y mejorando las interacciones comerciales.

📝 Descripción
La gestión eficaz de clientes es esencial para cualquier empresa orientada al cliente. Australens CRM facilita esta tarea mediante un sistema intuitivo y accesible que permite a los usuarios administrar su base de datos de clientes, hacer un seguimiento de las interacciones y acceder a información crítica con facilidad. La aplicación está pensada para empresas pequeñas y medianas que buscan optimizar sus procesos de ventas y mejorar la relación con sus clientes.

🚀 Características principales
Lista de Clientes: Visualiza y organiza la lista de clientes de manera clara, con la posibilidad de aplicar filtros para encontrar clientes específicos.
Registro y Edición: Añade nuevos clientes, edita la información existente y elimina registros obsoletos para mantener la base de datos actualizada.
Historial de Interacciones: Guarda y consulta notas sobre cada cliente, lo que facilita el seguimiento de las interacciones y mejora la continuidad de las relaciones.
Filtros Avanzados: Permite búsquedas rápidas y aplicar filtros personalizados sobre la base de datos de clientes para encontrar información específica de manera más eficiente.
🛠️ Tecnologías utilizadas
Backend: Django 4.2 (Python)
Base de datos: MySQL para almacenamiento seguro y escalable de datos.
Frontend: HTML y CSS para una interfaz de usuario limpia y fácil de usar.
📋 Requisitos previos
Python 3.9 o superior
Django (se instalará automáticamente con requirements.txt)
MySQL (necesario para la base de datos)
⚙️ Instalación y Configuración
Clonar el Repositorio
Clona el repositorio a tu máquina local:
bash
Copiar código
git clone https://github.com/NicolasMo3/Pagina-Web-.git
cd Pagina-Web-
Configurar el Entorno Virtual
Crea un entorno virtual y actívalo:
bash
Copiar código
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
Instalar Dependencias
Instala las dependencias necesarias:
bash
Copiar código
pip install -r requirements.txt
Configuración de la Base de Datos
Crea una base de datos MySQL para el proyecto.
Configura las credenciales de tu base de datos en el archivo settings.py en la sección DATABASES:
python
Copiar código
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_base_datos',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',  # o tu host de la base de datos
        'PORT': '3306',
    }
}
Realizar Migraciones y Ejecutar el Servidor
Aplica las migraciones:

bash
Copiar código
python manage.py migrate
Ejecuta el servidor de desarrollo:

bash
Copiar código
python manage.py runserver
Accede a la aplicación en http://127.0.0.1:8000.
