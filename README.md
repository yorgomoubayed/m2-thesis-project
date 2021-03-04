### Clone the repository
git clone https://git.embl.de/yelmoubayed/new-dp-service.git    
cd <repository>

### Create a virtual environment to isolate our package dependencies locally
~~~
python3 -m venv env 
~~~

~~~
source env/bin/activate  # On Windows use `env\Scripts\activate`    
~~~

### Install Django, Django REST framework and neomodel into the virtual environment
~~~
pip install django
~~~

~~~
pip install djangorestframework
~~~

~~~
pip install neomodel
~~~

### Django common command lines

When you make changes to your models, your database needs to understand how these changes might affect the database. This command automatically makes files that document these changes.
~~~
python manage.py makemigrations
~~~

This command you'll probably run the most of all commands. It means to run a emulated server on your local computer.
~~~
python manage.py runserver
~~~
