### Enviar formulario HTML a MySQL con Django

1.  Crear un entorno virtual, hay muchas formas

        Opción 1: Crear entorno virtual con el paquete virtualenv
        Si no tienes instalado virtualenv puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/
        pip install virtualenv ->Instalar de forma global
        virtualenv env ->Crear entorno
        virtualenv --version ->Ver la versión de virtualenv

        Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
        python -m venv env

2.  Activar entorno virtual

        . env/Script/activate ->para Windows
        . env/bin/activate -> Para Mac
        deactivate -->Para desactivar mi entorno virtual

3.  Instalar django desde el manejador de paquete de Python Pip, ya dentro del entorno virtual.

        python -m pip install Django
        pip install Django
        Nota: para instalar Django en una version especifica
        pip install Django==4.2.4

4.  Ver la versión de django instalada en el proyecto

        python -m django --version

5.  Instalar Driver para conectar Gestor de BD MySQL con Django

        pip install mysqlclient


7.  Crear el proyecto con django

        `django-admin startproject project_chatGPT .`
        El punto . es crucial le dice al script que instale Django en el directorio actual

        Ya en este punto se puede correr el proyecto que a creado Django,
        python manage.py runserver

8.  Crear mi primera aplicación en Django

        python manage.py startapp API_ChatGPT

9.  Instalar nuestra aplicación (API_ChatGPT) ya creada en el proyecto, en el archivo settings.py

        archivo settings.py
            INSTALLED_APPS = [
                ----,
                'API_ChatGPT',
            ]

10. Crear una clase en models.py la cual reprtesentara mi tabla en BD,(bd_django) preferiblemente los modelos
    se declaran en singular

        class HistorialChatPregunta(models.Model):
            id_historial = models.AutoField(primary_key=True)
            usuario = models.CharField(max_length=50, blank=False, null=False)
            pregunta = models.TextField()
            created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
            updated = models.DateTimeField(auto_now_add=False, auto_now=True)

            class Meta:
                db_table = "tbl_chat_preguntas"
                ordering = ['-created_at']


        class HistorialChatRespuestas(models.Model):
            id_respuesta = models.AutoField(primary_key=True)
            historial_id = models.ForeignKey(
                HistorialChatPregunta, on_delete=models.CASCADE)
            respuesta = models.TextField()
            created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
            updated = models.DateTimeField(auto_now_add=False, auto_now=True)

            class Meta:
                db_table = "chat_respuestas"
                ordering = ['-created_at']

11. crear la Base de Datos (bd_api_chatgpt) en MySQL

12. Editar el archivo settings.py del proyecto, cambiando los parametros de conexión a MySQL

        `
        DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',  # ENGINE es motor de BD
                    'NAME': 'bd_api_chatgpt',
                            'USER': 'root',
                            'PASSWORD': '',
                            'HOST': '127.0.0.1',
                            'PORT': '3306',
                }
            }
        `

13. Crear las migraciones y correrlas

        python manage.py makemigrations -> Creando migraciones
        python manage.py migrate         -> Correr migraciones

14. Correr el proyecto

        python manage.py runserver
        Revisar la consola y visitar la URL http://127.0.0.1:8000


15. Conectar las URLS de mi aplicación con el projecto, para esto vamos al archivo uls.py del projecto
    from django.urls import path, include

        urlpatterns = [
                path('admin/', admin.site.urls),
                path("", include('empleados.urls'))
        ]


16. Crear el archivo urls.py en la aplicación (bd_django_mysql)

        from django.urls import path
        from . import views

                urlpatterns = [
                        path('', views.inicio, name='inicio'),
                        path('registrar_empleado/', views.registrar_empleado,
                                name='registrar_empleado'),
                        path('empleados/', views.listar_empleados, name='listar_empleados'),
                ]


21. Crear el archivo requirements.txt para tener todos los paquetes del proyecto a la mano

        pip freeze > requirements.txt

        Nota: para instalar los paquetes solo basta ejecutar
        pip install -r requirements.txt

        
20. Correr archivo requirement.txt

        pip install -r requirements.txt



#### Resultado final

#####Formulario para registrar Empleado
![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/registrar-empleado-con-django-crud-urian-viera.png)

##### Lista de Empleados

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/lista-de-empleados-crud-django-urian-viera.png)

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍
