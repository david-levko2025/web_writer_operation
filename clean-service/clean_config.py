import os

class CleanConfig:

    def __init__(self):
        self.kafka_servers = os.getenv("KAFKA_SERVERS", "127.0.0.1:9092")
        self.kafka_topic_c = os.getenv("KAFKA_TOPIC_RAW", "Raw")
        self.kafka_topic_p = os.getenv("KAFKA_TOPIC_CLEAN", "Clean")

config = CleanConfig()