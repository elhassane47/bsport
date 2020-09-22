# bsport

## Run project using virtualenv



* env - using virtualenv here but any env manager should work

      $ sudo apt install build-essential python3.7 python-dev python3.7-dev python3-venv python3-pip  # depends on distro/os a lot
      $ pip3 install virtualenv
      $ python3 -m virtualenv env
      $ source env/bin/activate  
      $ pip install -r app/requirements.txt  
  

* Create the sql tables

      $ python manage.py migrate

* Create a user
	
      $ python manage.py createsuperuser

* Run the server

      $ python manage.py runserver

The website should be accessible at http://localhost:8000/  

## Run project using docker

Build and run the docker containers  

    $ cd resa && docker-compose up -d --build  
   
  
To update:  

    $ git pull  
    $ docker-compose up -d --build  

