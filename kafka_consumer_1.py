from kafka_methods import MessageConsumer

c = MessageConsumer(broker_host='localhost:9092', topic='scaranni_topic_1')

msgs = c.get_msgs_since_beginning()

for msg in msgs:
    print(msg)


