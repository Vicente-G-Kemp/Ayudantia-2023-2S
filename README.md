# Ayudantia-2023-2S
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