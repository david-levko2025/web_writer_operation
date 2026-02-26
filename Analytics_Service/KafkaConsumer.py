from confluent_kafka import Consumer
import json

from AnalyticsConfig import config


class KafkaConsumer:
    def __init__(self):

        consumer_config = {
            "bootstrap.servers": config.kafka_servers ,
            "group.id": "analytics_service",
            "auto.offset.reset": "earliest"
            }

        self.consumer = Consumer(consumer_config)     # type: ignore
        self.consumer.subscribe(["Clean"])


    def get_data_from_producer(self):
        msg = self.consumer.poll()
        if msg is None:
            return None
        elif msg.error():
            print(" Error:", msg.error())
            return None
        else:
            value = msg.value().decode("utf-8")  # type: ignore
            return json.loads(value)


        