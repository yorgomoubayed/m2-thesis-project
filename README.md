REST API created using Django, Neo4j and Neomodel.

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

## Django common command lines

#### Create constraints
~~~
python manage.py install_labels 
~~~

#### Track models changes
When you make changes to your models, your database needs to understand how these changes might affect the database. This command automatically makes files that document these changes.
~~~
python manage.py makemigrations
~~~

#### Run API server
You'll run this the most of all commands. It means to run a emulated server on your local computer.
~~~
python manage.py runserver
~~~

#### Open Django's Python shell
~~~
python manage.py shell
~~~

## Links to official documentations

* Django: <https://docs.djangoproject.com/en/3.1/>
* Neomodel: <https://neomodel.readthedocs.io/en/latest/>
* Neo4j: <https://neo4j.com/docs/>