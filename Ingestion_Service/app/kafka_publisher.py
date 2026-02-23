from confluent_kafka import Producer
import json

class KafkaPublisher:
    def __init__(self, servers):
        self.producer = Producer({'bootstrap.servers': servers})

    def publish_raw_event(self, topic, data):
        self.producer.produce(topic, json.dumps(data).encode('utf-8'))
        self.producer.flush()