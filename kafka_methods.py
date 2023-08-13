from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import TopicAlreadyExistsError
import json
import logging
import sys

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)],
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class KafkaManager:
    def __init__(self, broker_host='localhost:9092'):
        self.broker_host = broker_host
        self.broker = KafkaAdminClient(bootstrap_servers=self.broker_host)

    def create_topic(self, name, num_partitions=3, replication_factor=1):
        topic = NewTopic(name=name,
                         num_partitions=num_partitions,
                         replication_factor=replication_factor)
        try:
            self.broker.create_topics(new_topics=[topic])
            return "Topic created successfully"
        except TopicAlreadyExistsError:
            return "Topic already exists"


class MessageProducer:
    def __init__(self, broker_host, topic):
        self.broker_host = broker_host
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker_host,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                      acks='all',
                                      retries=3)

    def send_msg(self, msg):
        logging.info("Sending message.")
        future = self.producer.send(self.topic, msg)
        self.producer.flush()
        future.get(timeout=60)
        logging.info("Message sent successfully.")


class MessageConsumer:
    def __init__(self, broker_host, topic):
        self.broker_host = broker_host
        self.topic = topic

    def get_msgs_since_beginning(self):
        consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.broker_host,
        )

        consumer.partitions_for_topic(self.topic)
        consumer.seek_to_beginning()

        msgs = []

        records = consumer.poll(timeout_ms=1000)
        for _, consumer_records in records.items():
            for consumer_record in consumer_records:
                msgs.append(str(consumer_record.value.decode('utf-8')))
            continue
        return msgs

