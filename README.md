# Getting Started

First clone the repository from Github, and switch to the new directory:

    $ git clone https://github.com/dsteb/testapp_django.git
    $ cd testapp_django
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
Then simply apply the migrations:

    $ python manage.py migrate

If you need the test data apply the fixtures:

	$ python manage.py loaddata users
	$ python manage.py loaddata tweety

You can now run the development server which will give you more details:

    $ python manage.py runserver
