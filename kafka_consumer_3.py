from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer('scaranni_topic_1',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='A',
                         value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    print(f"Mensagem recebida: "
          f"Tópico: {message.topic}, "
          f"Partição: {message.partition}, "
          f"Offset: {message.offset}, "
          f"Timestamp: {message.timestamp}, "
          f"Chave: {message.key}, "
          f"Valor: {message.value}")
    print("-----")
