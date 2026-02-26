from confluent_kafka import Producer
import json

from ingestion_config import config
class KafkaPublisher:
    def __init__(self):
        self.producer = Producer({'bootstrap.servers': config.kafka_servers})

    def publish_raw_event(self,data):
        self.producer.produce(topic=config.kafka_topic ,value= json.dumps(data).encode('utf-8'))
        self.producer.flush()