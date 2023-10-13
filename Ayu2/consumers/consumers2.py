from kafka import KafkaConsumer, TopicPartition
import random

servidores_bootstrap = 'kafka:9092'
topics = ['temperatura']

grupo_consumidores = f'grupo_consumidores_{topics[0]}'

# Configurar el consumidor con el group_id
consumer = KafkaConsumer(
    bootstrap_servers=[servidores_bootstrap],
    group_id=grupo_consumidores,
)

# Especificar la partición desde la que queremos consumir
particion_especifica = TopicPartition(topics[0], 0)  # Selecciona la partición 0 del topic "temperatura"

# Asignar la partición específica al consumidor
consumer.assign([particion_especifica])

# Consumir mensajes de la partición asignada
for msg in consumer:
    print(f"Topic: {msg.topic}, Partición: {msg.partition}, Mensaje: {msg.value.decode('utf-8')}")
