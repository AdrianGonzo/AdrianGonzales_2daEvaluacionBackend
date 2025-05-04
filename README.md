# AdrianGonzales_2daEvaluacionBackend
## Microservicio gRCP para el consumo del endpoint usuarios/seguimientos_procesados en el Proyecto Podcast Bicentenario
Este proyecto implementa un microservicio utilizando gRPC que consume el backend de Podcast Bicentenario para gestionar los usuarios y creadores.
Este microservicio se encarga de:
- Obtener los seguidos de un usuario mediante su id
- Presentar la cantidad de creadores seguidos y sus id

Tecnologias Utilizadas
- Django
- gRPC
- dotenv
- Supabase
Instalación
- Clonar el repositorio
- Entrar al la carpeta raiz
```bash
cd AdrianGonzales_2daEvaluacionBackend
```
- Instalar dependencias
```bash
pip install django
```
```bash
pip install supabase
```
```bash
pip install psycopg2-binary
```
```bash
pip install djangorestframework django-cors-headers
```
```bash
pip install grpcio grpcio-tools
```
- Levantar el microservicio
```bash
python grpc_server.py
```
- Levantar el backend
```bash
python manage.py runserver
```
Uso
Realizar una petición GET a:   
- http://127.0.0.1:8000/usuarios/seguimientos_procesados/10
  Se puede cambiar el valor final por el id del usuario que se desee ver
Respuesta esperada
```json 
{ 
"total": 2, 
"creadores": ["6", "9"], 
"error": "" 
}
```
Estructura del Proyecto:                                                              
backend/                                                     
├── grpc_client/                                                                  
│   ├── __init__.py                                            
│   ├── seguimientos_pb2.py         #Generado                                     
│   ├── seguimientos_pb2_grpc.py    #Generado                                     
│   └── seguimientos.proto          #Definicion de servicios y mensajes                 
├──servidor_grpc.py                 #Codigo y lógica del Servidor de gRPC                   
├──urls.py                          #URLs que enrutan a las vistas                 
├── views.py                      #Vistas del Django  
manage.py
README.md 

Consideraciones:
- El endpoint no funciona si no se proporciona el id de un usuario
  
Pruebas:
- Se realizaron pruebas con Postman y los resultados de los GET mostraban lo esperado

Autor:
Adrian Gonzales, en cumplimento de la implementación de microservicios para el proyecto
