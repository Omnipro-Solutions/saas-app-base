# saas-app-base
Librería del modulo base para app de conexión a OMS

## Celery
Se recomienda la utilización de celery para el manejo de tareas programadas, colas y procesamiento en segundo plano, en los proyectos que sea necesario y se desee utilizar esta tecnología, se deben realizar las configuraciones respectivas, tal y como se explica en el presente documento.

También se puede ver la documentación oficial en este enlace: https://docs.celeryq.dev/en/v5.3.6/django/first-steps-with-django.html

## Configuración celery
A continuación se describe la manera en que se debe instalar Celery, configurar los parámetros iniciales y ejecutar este en un ambiente de pruebas y desarrollo

Use el administrador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar las siguientes librerías.

```bash
pip install celery
pip install redis
pip install django-celery-results
```

En preferencia, se recomienda utilizar las versiones aquí citadas:  
celery==5.3.6  
redis==5.0.1  
django-celery-results==2.5.1  

- ### Instalación base de de datos Redis para Celery:
    Celery requiere una base de datos noSql para su funcionamiento, en esta instalación se utilizará Redis.  
    Se puede seguir la siguiente documentación para su instalación en linux https://redis.io/docs/install/install-redis/install-redis-on-linux/  
    
    ```bash
    sudo apt install lsb-release curl gpg
    curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
    echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
    
    sudo apt-get update
    sudo apt-get install redis
    ```

Posterior a la instalación de Celery y Redis, se procederá a configurar los parámetros necesario para su ejecución:  

Importante: Estos parámetros deben s ser configurados en la aplicación donde se requiere la utilización de celery  

En la aplicación de django que se desee utilizar Celery, agregar estos parámetros en el archivo settings.py:  

```bash
# CONFIGURATION CELERY
CELERY_NAME_APP_DJANGO = "magento" # Nombre de proyecto ejemplo, si el proyecto de django tiene como nombre "math_application" este mismo valor debe ir aquí

CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0' #Broker de sistema de mensajería de tasks
RESULT_BACKEND = 'redis://127.0.0.1:6379/0' #Donde celery almacenará los resultados de las tareas

ACCEPT_CONTENT = ['json'] #Tipo de contenido aceptado al serializar datos
RESULT_SERIALIZER = 'json' # Especifica el serializador que Celery utilizará para serializar tanto los resultados como las tareas enviadas
TASK_SERIALIZER = 'json' # Especifica el serializador que Celery utilizará para serializar tanto los resultados como las tareas enviadas
TIMEZONE = 'UTC' # Define la zona horaria que Celery utilizará para programar tareas
RESULT_PERSISTENT = True # Indican que los resultados de las tareas y la información sobre las tareas (como su estado) se almacenarán de forma persistente, incluso después de reinicios del sistema.
CELERY_TASK_PERSISTENT = True
broker_connection_retry_on_startup = True # Habilita la funcionalidad de reintento de conexión al broker en el arranque

CELERY_MAX_RETRIES = 3 # Establecen el número máximo de reintentos de ejecución de una tarea
CELERY_SECONDS_TIME_TO_RETRY = 30 # Tiempo entre reintentos para una tarea si falla

# CONFIGURATION CELERY RESULTS
RESULT_EXTENDED = True # Habilita la extensión de resultados, que permite almacenar información adicional sobre el resultado de las tareas.
CELERY_CACHE_BACKEND = 'django-cache' # Configura el backend de caché y el backend de resultados en el contexto de un proyecto Django
CELERY_RESULT_BACKEND = 'django-db'
```

En el parámetro INSTALLED_APPS, añadir las librerías "django_celery_results" y "omni_pro_base"

Crear un archivo (al mismo nivél de settings.py), llamado celery.py y agregar el siguiente fragmento de codigo:

```python
import os

from celery import Celery
from magento.settings import CELERY_NAME_APP_DJANGO #Este import es un ejemplo, teniendo en cuenta que el proyecto tiene como nombre "magento"
from omni_pro_base.setting import CELERY_NAME_APP_DJANGO as OMNI_PRO_BASE_SETTING


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magento.settings')

app = Celery(CELERY_NAME_APP_DJANGO)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django apps.
app.autodiscover_tasks([CELERY_NAME_APP_DJANGO, OMNI_PRO_BASE_SETTING])


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
```

En el archivo __init__.py del proyecto de django, se debe agregar lo siguiente:
```python
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)
```

## Ejecutar celery:
Celery en este contexto es un complemento de django, con los pasos anteriores es suficiente para ejecutar Celery, para realizar esto se puede utilizar el siguiente comando:

```bash
celery -A magento worker --loglevel=INFO
```

Siendo la palabra "magento" el valor asignado en el parámetro CELERY_NAME_APP_DJANGO del settings.py del proyyecto

## Utilización celery en el proyecto
Se recomienda que en los proyectos de django donde se desee utilizar Celery, se cree una carpeta llamada task y dentro de esta, en archivos individuales, irán definidas las clases que contrndrán las tareas a ejecutar, ejemplo:

```python
from time import sleep
from magento.settings import CELERY_MAX_RETRIES, CELERY_SECONDS_TIME_TO_RETRY
from celery import shared_task, current_task


class TestTaskCelery:

    @staticmethod
    @shared_task(max_retries=CELERY_MAX_RETRIES, default_retry_delay=CELERY_SECONDS_TIME_TO_RETRY)
    def test_task_celery(x, y):
        try:
            sleep(2)
            return x + y

        except Exception as exc:
            print(f"Tarea fallida: {exc}")
            raise current_task.retry(exc=exc, countdown=2)
```

Los métodos que se van a crear como tareas en Celery, deberán llevar el siguiente decorador @shared_task y para ser invocados se debe hacer así:

```python
test_task_celery.delay(1, 2)
```

Con la palabra "delay" el sistema reconocerá que esta tarea debe ser encolada en Celery

