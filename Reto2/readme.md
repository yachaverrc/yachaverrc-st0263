# info de la materia: ST0263 Topicos especiales en telematica
#
## Estudiante: Yhilmar Andres Chaverra Castaño, yachaverrc@eafit.edu.co
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
#  Procesos comunicantes por API REST, RPC y MOM
#
# 1. breve descripción de la actividad

Este reto consiste en la implementación de una API Gateway el cual realiza la solicitud de 2 servicios, Uno de ellos consiste en una comunicación sincrónica a través de GRPC, y el otro es la implementación de un modelo de comunicación asincrónica (M.O.M.), estos servicios deben soportar concurrencia, además debe tener la capacidad de usar una u otra comunicación dependiendo de la disponibilidad, para el proceso de peticiones de los clientes usaremos API-REST con un servidor Flask, Se utilizará Grpc para la comunicación RPC y RabbitMQ o Apache Kafka para la comunicación MOM.


## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
En este caso pudimos cumplir bastantes criterios del proyecto, existe comunicación entre los servicios y la API Gateway, existen métodos que nos permiten listar los archivos que se encuentran en un directorio y poder comprobar la existencia de cada uno de ellos, también se pudo implementar el uso por defecto de un modelo sincrónico GRPC, y en caso de fallar el servicio mencionado se puede usar el servicio MOM, esto para mantener la tolerancia a fallos.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Fue un reto bastante interesante, y en este caso no pude hacerlo en el tiempo estipulado, pero concorde con el profesor una extensión de plazo y se pudieron lograr los objetivos de aprendizaje y los requisitos.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
La arquitectura es muy simple, existe una API Gateway el cual se comunica con 2 servicios a través de 2 procesos distintos, GRPC Y MOM, estos servicios son consultados a través del API Gateway usando Rest para hacer las solicitudes desde el navegador

# 3. Descripción del ambiente de desarrollo y técnico:

librerias: os, Flask, jsonify, grpc, sys, pika, uuid, futures.

Desarrollado en: Python 3.8.10


## como se compila y ejecuta.

Para la ejecución del proyecto se debe hacer uso de RabbitMQ para la gestión de las colas en el proceso del MOM, configurar una cola Request y una cola Response, y para usar el codigo implementado vamos a cada uno de los directorios y hacemos la ejecución con el comando python <Archivo.py>

El API lo ejecutamos en ApiGateway/main.py
El Grpc lo ejecutamos en GRPC/server.py
El MOM lo ejecutamos en MOM/Consumer.py

desde el navegador podemos hacer las peticiones correspondientes: 
    localhost/5000/list 
    localhost/5000/search/<filename>

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
en este caso haremos las especificaciones de los parametros del programa a traves del codigo, El GRPC se comunica a traves del puerto 50051



