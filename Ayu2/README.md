# Ayudantia-Kafka
joaquin.fernandez1@mail.udp.cl

Para levantar topologia de contenedores:
```sh
docker compose up --build
```
Para visualizar contenedores y sus estados:
```sh
docker ps -a
```
---
Para realizar pruebas pertinentes entre par producer y consumer colocar los siguientes comandos:

Entran al producer
```sh
docker exec -it producer_kafka bash
```
Entran al consumer:
```sh
docker exec -it consumer_kafka bash
```
## *Caso1*
Para el primer caso que es de trabajo con Consumer Groups, ejecutar el siguiente comando dentro de la bash del contenedor producer (se coloca un numero como argumento ya que está usando threads para que no hayan conflictos con enviados anteriores):
```sh
python3 producers.py 5
```
Luego dentro de la bash del consumer ejecutan el siguiente comando:
```sh
python3 consumers.py
```
nota: el producer estara enviando y el consumer se demora un poco en establecer la conexión con el producer en caso que se demore un poco en recibir la información, ahí tendrán que esperar.

## *Caso2*
Para el segundo caso que es de trabajo con particiones, está la conexión simplificada entre topics lo importante es el trabajo de los subtopics y estos vendíran a ser las particiones como lo es en el ejemplo de temperatura con casos como celcius, kelvin y fahrenheit.

Aunque deben de entrar en otra bash a kafka esto con la razón de que kafka debe de identificar que las particiones existen y están asociadas al topic respectivo y pueden hacerlo con el siguiente comando (cabe recordar que deben de entrar a la consola del servicio kafka (docker exec -it kafka bash)):
```sh
kafka-topics.sh --alter --bootstrap-server kafka:9092 --partitions 3 --topic temperatura
```

Nuevamente para la ejecución del producer deben de colocar el siguiente comando:
```sh
python3 producers2.py 5
```

Nuevamente para la ejecución del consumer deben de colocar el siguiente comando:
```sh
python3 consumers2.py
```

## *Caso3*
Para el tercer caso se aplicó el uso de brokers, ya que se trabaja con clusters de kafka entonces se tendrían cada topic adherido con un contenedor en específico casi como un server de kafka que trabaja con varios producers a la vez. \
Primero deben de ejecutar el docker-compose-brokers.yml para levantar la topología mediante el siguiente comando:
```sh
docker compose -f docker-compose-brokers.yml up --build
```
Por lo que para ejecutar cada contenedor se deben de aplicar los siguientes comandos:
```sh
docker exec -it producer_kafka bash
docker exec -it producer_kafka2 bash
docker exec -it producer_kafka3 bash
```
Aquí deben de aplicar en cada uno de ellos el siguiente comando:\
Para el producer dentro del primer contenedor:
```sh
python3 producers3.py 4 temperatura
```
Para el producer dentro del segundo contenedor:
```sh
python3 producers3.py 4 porcentaje_humedad
```
Para el producer dentro del tercer contenedor:
```sh
python3 producers3.py 4 posicion
```
Para el consumer:
```sh
python3 consumers3.py
```
Y debería de aparecer en el consumer los mensajes de cada uno de los topics asociados al servidor de Kafka procedentes de cada contenedor.\
Por último para bajar la topología deben de ejecutar el siguiente comando:
```sh
docker compose -f docker-compose-brokers.yml down -v
```