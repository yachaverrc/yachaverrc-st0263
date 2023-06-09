# Universidad EAFIT
# ST0263 TÓPICOS ESPECIALES EN TELEMÁTICA, 2023-1
## Laboratorio 5.1

## Evidencias de la creación de cluster AWS EMR en Amazon.

Amazon EMR (Elastic MapReduce) es un servicio web, el cual permite procesar grandes cantidades de datos de manera rápida. Con Amazon EMR, puedes crear y gestionar clústeres de Amazon EC2 (Elastic Compute Cloud) y utilizar aplicaciones de procesamiento de datos como Apache Spark, Apache Hive y Apache Hadoop.

### Creación del Cluster 
Seleccionamos las siguientes aplicaciones para nuestro clúster:
#### HCatalog 3.1.2
#### Hadoop 3.2.1
#### Hive 3.1.2
#### Hue 4.9.0
#### JupyterEnterpriseGateway 2.1.0
#### JupyterHub 1.2.0
#### Livy 0.7.0
#### Spark 3.1.1
#### Sqoop 1.4.7
#### Tez 0.9.2
#### Zeppelin 0.9.0

![1](https://github.com/yachaverrc/yachaverrc-st0263/assets/60229713/29988f30-3091-40f4-ab62-113635f1f373)
### Acceso a través de SSH
![9](https://github.com/yachaverrc/yachaverrc-st0263/assets/60229713/8a1d8237-f465-43b0-88b1-685acd743520)
Antes de acceder a las aplicaciones dentro de nuestro clúster, debemos habilitar los puertos en la opción "bloquear el acceso al público" y en el grupo de seguridad de la instancia principal.

#### 22, para el SSH.
#### 8888, para Hue.
#### 9443, para Jupyter.
#### 8090, para Zeppelin.

Estas capturas las tomamos como evidencia del seguimiento de los pasos del LAB5.1.
### Acceso a Hue
![2](https://github.com/yachaverrc/yachaverrc-st0263/assets/60229713/b38ee28f-4be0-4d06-b97b-4be8e5831451)
### Mainpage Database Hue
![3](https://github.com/yachaverrc/yachaverrc-st0263/assets/60229713/a808f8fd-cf08-400d-9af8-e688b7c85b15)
### Acceso a JupyterHub
![4](https://github.com/yachaverrc/yachaverrc-st0263/assets/60229713/ca8e209e-97bc-44df-a1f3-caaac36a64d7)
### Mainpage JupyterHub
![5](https://github.com/yachaverrc/yachaverrc-st0263/assets/60229713/b75eeb2a-0449-42a8-9882-7fb42011fd36)
### Revisamos variables de entorno
![6](https://github.com/yachaverrc/yachaverrc-st0263/assets/60229713/64cd0d7c-1579-4374-b9f7-9773c8720943)
### Acceso a Zeppelin
![7](https://github.com/yachaverrc/yachaverrc-st0263/assets/60229713/ff7655b7-3137-44a6-9789-5e1d7305a601)
### Persistencia en S3
![8](https://github.com/yachaverrc/yachaverrc-st0263/assets/60229713/2676adc7-0d34-4741-84f2-39949e184a45)
