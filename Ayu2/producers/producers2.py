from kafka import KafkaProducer
from json import dumps
import time
import random
import string

servidores_bootstrap = 'kafka:9092'
topic_temperatura = 'temperatura'

productor = KafkaProducer(bootstrap_servers=[servidores_bootstrap], value_serializer=lambda x: dumps(x).encode('utf-8'))  
# Se añadió value_serializer para simplificar el envío de mensajes JSON

def generar_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 20)))

def enviar_temperatura():
    topic = topic_temperatura
    while True:
        temperatura = round(random.uniform(10, 30), 1)
        mensaje = {
            "timestamp": int(time.time()),
            "id": generar_id(),
            "temperatura": temperatura
        }
        productor.send(topic, mensaje)  # No es necesario convertir mensaje a JSON aquí, ya que se hace automáticamente con value_serializer
        print('Enviando JSON:', mensaje)  # Se imprime el diccionario mensaje directamente para mejorar la legibilidad
        time.sleep(3)

if __name__ == "__main__":
    enviar_temperatura()
