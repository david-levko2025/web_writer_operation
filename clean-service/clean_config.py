import os

class CleanConfig:

    def __init__(self):
        self.kafka_servers = os.getenv("KAFKA_SERVERS", "127.0.0.1:9092")
        self.kafka_topic = os.getenv("KAFKA_TOPIC", "raw_images_topic")

config = CleanConfig()