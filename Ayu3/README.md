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

---
## Tutorial Hadoop

Primero que todo ya deben de tener la topología levantada. Posterior de ello deben de visualizar los respectivo directorios con los cuales van a trabajar vendrían a ser examples y buscador. \
\
Otro detalle de suma relevancia, si es que están en windows, deben de cambiar el interprete de crlf a lf; puesto que si no lo hacen puede que les genere conflico para la lectura y ejecución de ciertos archivos al momento de realizar acciones de haddop como la sincronización de archivos sh y también archivos python en este caso que interactuan con la consola.\
\
**Los archivos que deben cambiar son mapper.py, reducer.py y docker-entrypoint.sh** 

Ahora  lo para trabajar con hadoop usaremos comandos basicos dentro de su repertorio y esto con el modivo de que es un manejador de archivos distribuido con nombre hdfs (Hadoop Distributed Files System). \
\
Posterior a lo anterior deben de configurar un usuario que administrará todos los comandos y por ello es necesario que sigan las siguientes instrucciones y/o comandos:

**[1]** Se creará un respectivo directorio para gestionar las acciones del usuario hduser (es imporatnte que tenga este nombre para todos los comandos):
