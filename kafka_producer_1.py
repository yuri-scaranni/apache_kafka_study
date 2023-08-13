from kafka_methods import MessageProducer
import time
import random
import uuid

p = MessageProducer(broker_host='localhost:9092', topic='scaranni_topic_1')

counter = 0
while True:
    time.sleep(2)
    magic_number = random.randint(1000, 9999)
    magic_hash = str(uuid.uuid4())

    data = {'counter': counter, 'magic_number': magic_number, 'magic_hash': magic_hash}

    p.send_msg(data)

    counter += 1
