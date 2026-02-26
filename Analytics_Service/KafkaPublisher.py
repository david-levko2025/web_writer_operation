from confluent_kafka import Producer
import json

from AnalyticsConfig import config

class KafkaPublisher:
    def __init__(self):
        self.producer = Producer({'bootstrap.servers': config.kafka_servers})

    def publish_raw_event(self,data):
        self.producer.produce(topic=config.kafka_topic_p ,value= json.dumps(data).encode('utf-8'))
        self.producer.flush()