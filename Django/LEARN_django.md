# WHAT I LEARNT:

## DJANGO PROJECT:
* A django project is modular in structure to encourage reuse; Each module is called an app and has its own set of files; Django project has a subfolder with same name as the project and it contains the config files;

* Django follows Model View Template architecture; User requrested URLs are mapped to Views (through urls.py) and Views (stored in views.py in the form of functions) take the data from Model(usually DB, ORM type, stored in models.py) and then sends it to the Template (HTML) and also applies rendering logic to render django tags into the HTML code and finally the page is loaded to the user;

* When adding a new app to a project:
    - add the app to the installed_apps in the project settings file
    - and for every view:
        - write the function for view (urls.py)
        - map the view to a domain url (views.py)
    - ```path('', include('app_name.urls'))``` add the list of new urls of this app to the project's urls file (When renaming a project, make sure to update the url lists, and also the app name in apps.py of that app)

* ```<model_instance_name>.save()``` when save() is called, Django checks if the instance has a primary key;
    - instance has primary key: django performs UPDATE operation
    - instance doesn't have primary key: django performs CREATE operation 

## MIGRATIONS:
* Can be considered as a VCS for our Database Schema;

    - ```makemigrations``` command is run to generate SQL commands for the tables in the database; this command is run when changes are done to the model;

    - ```migrate``` command is responsible for applying and unapplying migrations;

    - ```showmigrations``` command lists a project's migrations and their status;

    - ```sqlmigrate``` command displays the SQL commands for a migration;

## DJANGO REST FRAMEWORK

### Serializers:
* converting complex Django model instances into Python datatypes that can be easily rendered into JSON/XML types

    - **Serialization**: Complex Model Instances -----> Python datatypes -----> JSON/XML

    - **Deserialization**: Stream -----> Python datatypes -----> Complex Model Instances

### Requests and Responses
* DRF request object extends HTTPRequest

* DRF response object extends HTTPResponse

* request.POST (django) vs request.data (DRF)
    * request.POST - can be used only for form submissions

    ``` python
    def my_view(request):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            # Process form data here
    ```

    ``` py
    from django.http import HttpRequest, HttpResponse
    def my_view(request: HttpRequest) -> HttpResponse:
        if request.method == 'POST':
            name = request.POST.get('name')
            return HttpResponse(f'Hello, {name}')
    ```

    * request.data - can be used for handling any type of request data (POST, PUT, PATCH, GET); supports parsing both JSON payloads and form data 

    ``` python
    def my_api_view(request):
        if request.method == 'POST':
            name = request.data['name']
            email = request.data['email']
            # Process data (JSON or form data) here
    ```

    ``` py
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import status

    class MyAPIView(APIView):
        def post(self, request):
            name = request.data.get('name')
            return Response({'message': f'Hello, {name}'}, status=status.HTTP_200_OK)
    ```

* HTTP codes for CRUD operations:

    **2xx Success**
    - 200: OK (GET, PUT)
    - 201: Created (POST)
    - 204: No Content (DELETE)

    **4xx Client Errors**
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 404: Not Found
    - 405: Method Not Allowed
    - 409: Conflict
    - 422: Unprocessable Entity

    **5xx Server Errors**
    - 500: Internal Server Error
    - 502: Bad Gateway
    - 503: Service Unavailable