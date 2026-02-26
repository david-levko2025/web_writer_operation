from confluent_kafka import Producer
import json
import os

from clean_config import config
class KafkaPublisher:
    def __init__(self):

        producer_config = {"bootstrap.servers": config.kafka_servers}
        self.producer = Producer(producer_config)  # type: ignore

    def produce_data(self,data):
        value = json.dumps(data).encode("utf-8")
        self.producer.produce(topic=config.kafka_topic_p,value=value)
        self.producer.flush()