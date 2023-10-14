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