from kafka import KafkaConsumer

consumer = KafkaConsumer('scaranni_topic_1',
                         group_id='A',
                         auto_offset_reset='earliest')
for msg in consumer:
    print(msg)


