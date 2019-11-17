# microservice-shop
Laboratory work on the course "Software Development Technology"  

This is an example of a simple online shop based on microservice architecture.  

## Technology Stack

- Nginx 
- uWSGI 
- Django
- Django REST Framework
- Swagger UI
- SQlite
- Docker

## Build and run 

To start all services:

```
docker-compose up --build
```

To start a specific service:

``` 
cd <path_to_service> 
docker build -t <service_name> . 
docker run -d -p 80:80 service_name>
```
 

## Contributing
