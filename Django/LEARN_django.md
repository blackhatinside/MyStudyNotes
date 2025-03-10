# WHAT I LEARNT:

## DJANGO PROJECT:
* A django project is modular in structure to encourage reuse; Each module is called an app and has its own set of files; Django project has a subfolder with same name as the project and it contains the config files;

* Django follows Model View Template architecture; User requrested URLs are mapped to Views (through urls.py) and Views (stored in views.py in the form of functions) take the data from Model(usually DB, ORM type, stored in models.py) and then sends it to the Template (HTML) and also applies rendering logic to render django tags into the HTML code and finally the page is loaded to the user;

* When adding a new app to a project:
    - add the app to the installed_apps in the project settings file
    - and for every view:
        - write the function for view (urls.py)
        - map the view to a domain url (views.py)
    - ```path('', include('app_name.urls'))```: add the list of new urls of this app to the project's urls file (When renaming a project, make sure to update the url lists, and also the app name in apps.py of that app)

- ```<model_instance_name>.save()```: when save() is called, Django checks if the instance has a primary key;
    - instance has primary key: django performs UPDATE operation
    - instance doesn't have primary key: django performs CREATE operation 

## MIGRATIONS:
* Can be considered as a VCS for our Database Schema;

    - ```makemigrations``` command is run to generate SQL commands for the tables in the database; this command is run when changes are done to the model;

    - ```migrate``` command is responsible for applying and unapplying migrations;

    - ```showmigrations``` command lists a project's migrations and their status;

    - ```sqlmigrate``` command displays the SQL commands for a migration;

## CELERY:
Segregation and temporary holding is done by message queue, a part of the message broker; and exchanges in message broker use binding rules for segregation of tasks into different storage queues. Task queues are basically { message queues + execution logic, scheduling and management }

User/Client/Consumer sends the task to the application in the form of message (message passing) and the celery based app then enqueues the task into the Message broker (Redis which is FIFO based) and then the celery worker machines which are listening to this celery queue take up the task on arrival into the queue and then try to process these tasks by spawning child processes or threads (concept of execution pool) and finally send back the result to a backend result queue which is later on used by the user or client. And also if the user wishes to know the progress of the task he can make use of client API to check task completion status through web sockets. And also CPU intensive tasks are done by preforks and I/O intensive tasks are done by threads and solo doesnt spawn any sub processes and instead tries to do the task by itself hence it is faster than prefork and thread pool. Concurrency level should be less than or equal to the number of CPU cores for true parallelism.

so basically the exchange, binding rules, different queues are all part of message broker and the tasks are sent to appropriate queues for the workers to process them.
