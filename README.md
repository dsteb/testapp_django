# Getting Started

First fork the repository from Github, clone it, and switch to the new directory:

    $ git clone https://github.com/USERNAME/testapp_django.git
    $ cd testapp_django
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server which will give you more details:

    $ python manage.py runserver


If you want a quick overview of what you'll be building you can see it here: https://gist.github.com/Nikola-K/e25d8bea233d4ffa59d526851cc92fb8
