REST API created using Djano, Neo4j and Neomodel.

### Clone the repository
~~~
git clone https://git.embl.de/yelmoubayed/new-dp-service.git    
cd <repository>
~~~

### Create a virtual environment to isolate our package dependencies locally
~~~
python3 -m venv env 
~~~
~~~
source env/bin/activate #On Linux and MacOS  
~~~
~~~
env\Scripts\activate #On Windows    
~~~

### Install requirements
~~~
pip install -r requirements.txt
~~~

### To add new requirements if needed 
~~~
pip freeze > requirements.txt
~~~

### Django common command lines

#### Create constraintes
~~~
python manage.py install_labels 
~~~

#### Track models changes
When you make changes to your models, your database needs to understand how these changes might affect the database. This command automatically makes files that document these changes.
~~~
python manage.py makemigrations
~~~

#### Run API server
This command you'll probably run the most of all commands. It means to run a emulated server on your local computer.
~~~
python manage.py runserver
~~~

#### Open Django's Python shell
~~~
python manage.py shell
~~~
