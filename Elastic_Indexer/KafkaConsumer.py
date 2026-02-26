from confluent_kafka import Consumer
import json

from IndexerConfig import config

class KafkaConsumer:
    def __init__(self):
        
        
        consumer_config = {
            "bootstrap.servers": config.kafka_servers ,
            "group.id": "elastic_service",
            "auto.offset.reset": "earliest"
                           }
        topics = [config.kafka_topic_1,config.kafka_topic_2,config.kafka_topic_3]
        self.consumer = Consumer(consumer_config)     # type: ignore
        self.consumer.subscribe(topics)


    def get_data_from_producer(self):
        msg = self.consumer.poll()
        if msg is None:
            return None
        elif msg.error():
            print("Error:", msg.error())
            return None
        else:
            value = msg.value().decode("utf-8")  # type: ignore
            return json.loads(value)