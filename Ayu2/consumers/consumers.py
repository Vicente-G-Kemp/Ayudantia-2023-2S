from kafka import KafkaConsumer, TopicPartition
import random

servidores_bootstrap = 'kafka:9092'
topics = ['temperatura']

topic_elegido = random.choice(topics)
grupo_consumidores = f'grupo_consumidores_{topic_elegido}'

# Configurar el consumidor con el group_id
consumer = KafkaConsumer(
    bootstrap_servers=[servidores_bootstrap],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=grupo_consumidores,
    value_deserializer=lambda x: x.decode('utf-8')
)

# Obtener las particiones para el topic elegido
particiones = consumer.partitions_for_topic(topic_elegido)

# Imprimir el topic y sus particiones
print(f"Topic: {topic_elegido}")
for particion in particiones:
    print(f" - Partición: {particion}")

# Consumir mensajes de todas las particiones del topic elegido
for particion in particiones:
    tp = TopicPartition(topic_elegido, particion)
    consumer.assign([tp])
    for mensaje in consumer:
        print(f"Mensaje de la partición {mensaje.partition()}: {mensaje.value}")

# Cerrar el consumidor para liberar recursos
consumer.close()