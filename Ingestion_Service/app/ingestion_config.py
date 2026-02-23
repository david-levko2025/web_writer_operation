import os

class IngestionConfig:
    def __init__(self):
        self.kafka_servers = os.getenv("KAFKA_SERVERS", "127.0.0.1:9092")
        self.kafka_topic = os.getenv("KAFKA_TOPIC", "raw_images_topic")
        self.images_path = os.getenv("IMAGES_PATH", "../tweet_images")
        self.loader_url = os.getenv("LOADER_URL", "http://127.0.0.1:8080/metadata/upload")