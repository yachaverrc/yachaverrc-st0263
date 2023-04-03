
# info de la materia: ST0263 Topicos especiales en telematica
#
## Estudiante: Yhilmar Andres Chaverra Castaño, yachaverrc@eafit.edu.co
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

# Aplicación Monolítica con Balanceo y Datos Distribuidos (BD y archivos)
  
# 1. breve descripción de la actividad
El reto consiste en un Desplige CMS de Wordpress usando contenerodes (Docker) en una arquitectura de alta disponibilidad, usando un dominio y una certificacion SSL para protocolo HTTPS, este proyecto tendra 5 componentes, un balanceador de carga en nginx, 2 servidores Wordpress, ademas de un servidor SQL para base de datos y por ultimo un NFSServer. esto desplegado en maquinas virtuales Google GPC.
  
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

En general, se cumplieron con la mayoría de los requerimientos funcionales y no funcionales propuestos por el profesor. el balanceo de cargas, la implementacion del NFSServer, los sistemas de Wordpress etc. 

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

No se pudo cumplir con el requisito de implementar un certificado SSL para las conexiones seguras a través de HTTPS. ademas que por motivos economicos y de la falta de un medio de pago como la targeta de credito, no fue posible comprar un dominio. y la plataforma de Freenom ya no esta disponible.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

Para este proyecto se utilizo la arquitectura propuesta por el profesor en el enunciado del reto.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## como se compila y ejecuta.

- Para La ejecucion del proyecto en las maquinas de Google GCP, usando los contenedores de Docker, se debe ir a la carpeta de cada uno de los componentes y ejecutar el archivo docker-compose.yml con el comando ´docker-compose -f <nombre del archivo> up´.

  
## detalles del desarrollo.
  Para todo el desarrollo de este Reto, Se utilizo Google Cloud Platform (GCP) haciendo uso de IaaS, usando maquinas virtuales de Compute Engine. Se utilizaron contenedores de Docker usando Docker Compose para los componentes de la aplicación en WordPress, la base de datos y el balanceador de carga. y finalmente, para el servidor NFS, se hizo la configuracion del host directamente en la máquina virtual.
  
## detalles técnicos
  - Tipo de maquina virtual: e2-Small.
  - Sistema operativo: Ubuntu 18.04 LTS.
  - Docker version 20.10.21.
  - Docker-compose version 1.17.1.
  - Base de datos: MySQL 5.7.
  - Balanceador de carga: NGINX.
  - CMS: WordPress.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
  Los diferentes parámetros se configuran en los archivos de Docker Compose, donde se especifica la dirección IP, los puertos, la conexión a la base de datos, las variables de ambiente, entre otros.
  
![Screenshot_20230403_064914](https://user-images.githubusercontent.com/60229713/229581047-6f51f509-0908-4878-89fa-f55809f6b98b.png)
  
## Organización del código por carpetas

![Screenshot_20230403_064855](https://user-images.githubusercontent.com/60229713/229581184-206c6e2a-68ee-481f-9db9-85266d03cf7d.png)

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## IP o nombres de dominio en nube o en la máquina servidor.
  - IPs:
    LB: http://34.28.3.220/
    wordpress1: 34.171.105.116
    wordpress2: 34.170.44.74
  
  - Dominio: No Disponible

## como se lanza el servidor.
Para la ejecucion de el proyecto en necesario iniciar las maquinas virtuales en Google GCP.

## una mini guia de como un usuario utilizaría el software o la aplicación
Para acceder en este caso solo debes entrar a travez de apuntar a el LB (Load Balancer) y podras acceder al servicio en Wordpress.

## Resultados o pantallazos 
  
![Screenshot_20230403_065849](https://user-images.githubusercontent.com/60229713/229581482-eead2afd-f96e-4190-b636-d6a7ea35933b.png)


![Screenshot_20230403_064825](https://user-images.githubusercontent.com/60229713/229581343-5e483848-0dc1-4f0c-8d07-7e1dece7e09e.png)

# referencias:
Overview of docker compose CLI: https://docs.docker.com/compose/reference/
How To Set Up an NFS Mount on Ubuntu 22.04: https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-22-04
How to Connect a Domain to a Server or Hosting: https://www.namecheap.com/support/knowledgebase/article.aspx/9837/46/how-to-connect-a-domain-to-a-server-or-hosting/
