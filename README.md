REST API prototype created using Django, Neo4j, Neomodel and Django REST Framework (DRF).

## Clone the repository
~~~
git clone https://git.embl.de/yelmoubayed/new-dp-service.git    
cd <repository>
~~~

## Create a virtual environment to isolate the package dependencies locally
~~~
python3 -m venv env 
~~~
~~~
source env/bin/activate #On Linux and MacOS  
~~~
~~~
env\Scripts\activate #On Windows    
~~~

## Install requirements
~~~
pip install -r requirements.txt
~~~

## Add new requirements if needed 
~~~
pip freeze > requirements.txt
~~~

## Django's most important command lines

This command is used to create a project
~~~
django-admin startproject <project name>
django-admin.py startproject <project name>
~~~

This command is used to create an application inside a project
~~~
python manage.py <app name>
~~~

This command applies migrations
~~~
python manage.py migrate
~~~

This command creates new migrations based on the changes you have made to your models
~~~
python manage.py makemigrations
~~~

This command opens a python shell to test query sets
~~~
python manage.py shell
~~~

This command runs an emulated server on your local machine
~~~
python manage.py runserver <optional port number>
~~~

This command creates a super user to access the admin panel
~~~
python manage.py createsuperuser
~~~

This command creates a cache table 
~~~
python manage.py createcachetable
~~~

This command applies neomodel constraints
~~~
python manage.py install_labels 
~~~

## Links to official documentations

* **Django:** <https://docs.djangoproject.com/en/3.1/>
* **Neomodel:** <https://neomodel.readthedocs.io/en/latest/>
* **Neo4j:** <https://neo4j.com/docs/>
* **DRF:** <https://www.django-rest-framework.org/>, **DRF/serializers:** <https://www.django-rest-framework.org/api-guide/serializers/>
* **Serializing neomodel data tutorial:** <https://neo4j-examples.github.io/paradise-papers-django/tutorial/part01.html>