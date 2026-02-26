import os

class AnalyticsConfig:
    def __init__(self):
        self.kafka_servers = os.getenv("KAFKA_SERVERS", "127.0.0.1:9092")
        self.kafka_topic = os.getenv("KAFKA_TOPIC", "Analytics")

config = AnalyticsConfig()