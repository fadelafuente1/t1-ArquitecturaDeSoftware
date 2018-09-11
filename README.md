# Tarea 1 Arquitectura de sistemas de software 2018-2
#### Felipe De la Fuente

- La aplicación se encuentra disponible en http://charette10.ing.puc.cl/
- Se utilizo la siguiente documentación como referencia para crear la aplicación web: https://docs.djangoproject.com/es/2.1/intro/tutorial01/
- Se utilizo la siguiente documentación como referencia para dejar en ambiente de producción: https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
## Tecnologias utilizadas
- Python 3.7
- Django 2.1
- postgreSQL
- virtualenv
- nginx
- guarnicorn
## Instalación de dependencias

´´´
brew install python3
pip install django
pip install psycopg2
pip install virtualenv
pip install nginx
pip install guarnicorn
´´´

## Testeo en development
Dentro de t1-ArquitecturaDeSoftware
´´´
python3 manage.py migrate
python3 manage.py runserver
´´´
## Actualización en servidor
Ante cualquier cambio:
´´´
sudo systemctl restart gunicorn
´´´
