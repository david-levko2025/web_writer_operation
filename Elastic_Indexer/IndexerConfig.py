import os

class IndexerConfig:
    def __init__(self):
        self.kafka_servers = os.getenv("KAFKA_SERVERS", "127.0.0.1:9092")
        self.elasticsearch_server = os.getenv("ELASTIC_SERVER",'http://localhost:9200')
        self.kafka_topic_1 = os.getenv("KAFKA_TOPIC_RAW","Raw")
        self.kafka_topic_2 = os.getenv("KAFKA_TOPIC_CLEAN","Clean")
        self.kafka_topic_3 = os.getenv("KAFKA_TOPIC_ANALYTICS","Analytics")
config = IndexerConfig()