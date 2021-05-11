Data processing service prototype created using Django, Neo4j, Neomodel and Django REST Framework (DRF).

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

## Django command lines

Create a project
~~~
django-admin startproject <project name>
django-admin.py startproject <project name>
~~~

Create an application inside a project
~~~
python3 manage.py <app name>
~~~

Apply migrations
~~~
python3 manage.py migrate
~~~

Create new migrations based on the changes made to the models
~~~
python3 manage.py makemigrations
~~~

Open a python shell to test query sets
~~~
python3 manage.py shell
~~~

Run an emulated server on the local machine
~~~
python3 manage.py runserver <optional port number>
~~~

Create a super user to access the admin panel
~~~
python3 manage.py createsuperuser
~~~

Create a cache table 
~~~
python3 manage.py createcachetable
~~~

Run tests
~~~
python3 manage.py test <optional test module name>
~~~

Apply constraints and indexes on labels for the node definitions. This should be executed after any schema changes
~~~
python3 manage.py install_labels
~~~

Delete all nodes in the database.
~~~
python3 manage.py clear_neo4j
~~~

## Links to documentations

* **Django:** <https://docs.djangoproject.com/en/3.1/>
* **Neomodel:** <https://neomodel.readthedocs.io/en/latest/>
* **Neo4j:** <https://neo4j.com/docs/>
* **DRF:** <https://www.django-rest-framework.org/>
* **Serializing neomodel data:** <https://neo4j-examples.github.io/paradise-papers-django/tutorial/part01.html>