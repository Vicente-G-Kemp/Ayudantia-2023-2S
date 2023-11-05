# Ayudantia-Hadoop
joaquin.fernandez1@mail.udp.cl

Para levantar topologia de contenedores:
```sh
docker compose up --build
```
Para visualizar contenedores y sus estados:
```sh
docker ps -a
```
Para entrar a contenedores:
```sh
docker exec -it name_service_o_id bash
```
Para bajar arquitectura junto a los volumenes usar el siguiente comando:
```sh
docker compose down -v
```
Para borrar cache usar el siguiente comando luego de bajar todos los contenedores
```sh
docker system prune -a
```
Para borrar contenedores a mano sin la necesidad de usar el -v en el comando compose down:
```sh
docker volume rm $(docker volume ls -q)
```