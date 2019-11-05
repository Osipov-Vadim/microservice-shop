# microservice-shop
Laboratory work on the course "Software Development Technology"
## Contributing
Install requirements:
```
    pip install -r requirements.txt
```
To start the Catalog-Service use:
```
    cd Catalog-Service
    python manage.py makemigrations && python manage.py migrate
    python manage.py runserver 7777
```
To start the Order-Service use:
```
    cd Order-Service
    python manage.py makemigrations && python manage.py migrate
    python manage.py runserver 7778
```
To start the Payment-Service use:
```
    cd Payment-Service
    python manage.py makemigrations && python manage.py migrate
    python manage.py runserver 7779
```
