from kafka import KafkaProducer
from json import dumps
import time
import random
import string

servidores_bootstrap = 'kafka:9092'
topic_temperatura = 'temperatura'

productor = KafkaProducer(bootstrap_servers=[servidores_bootstrap], value_serializer=lambda x: dumps(x).encode('utf-8'))

def generar_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 20)))

def enviar_temperatura():
    topic = topic_temperatura
    while True:
        temperatura = round(random.uniform(10, 30), 1)
        id_mensaje = generar_id()
        mensaje = {
            "timestamp": int(time.time()),
            "id": id_mensaje,
            "temperatura": temperatura
        }
        productor.send(topic, value=mensaje, key=id_mensaje.encode())  # Se especifica la clave de partición con el parámetro key
        print(id_mensaje.encode())
        print('Enviando JSON:', mensaje)
        time.sleep(3)

if __name__ == "__main__":
    enviar_temperatura()
