import os

from .ingestion_config import IngestionConfig
from .mongo_loader_client import MongoLoaderClient
from .kafka_publisher import KafkaPublisher
from model.ocr_engine import OCREngine
from model.metadata_extractor import MetadataExtractor

class IngestionOrchestrator:
    def __init__(self):
        self.config = IngestionConfig()
        self.ocr = OCREngine()
        self.meta = MetadataExtractor()
        self.loader = MongoLoaderClient(self.config.loader_url)
        self.kafka = KafkaPublisher(self.config.kafka_servers)

    def run_pipeline(self):
        if not os.path.exists(self.config.images_path):
            print(f"path {self.config.images_path} not found")
            return

        for filename in os.listdir(self.config.images_path):
            if filename.lower().endswith((".png")):
                full_path = os.path.join(self.config.images_path, filename)
                print(f"processing...: {filename}")

                metadata = self.meta.extract(full_path)
                raw_text = self.ocr.extract_text(full_path)

                loader_res = self.loader.forward_binary(full_path)
                mongodb_id = loader_res.get("mongodb_id") if loader_res else None

                raw_event = {
                    "image_id": metadata["image_id"],
                    "mongodb_id": mongodb_id,
                    "raw_text": raw_text,
                    "metadata": metadata
                }
                self.kafka.publish_raw_event(self.config.kafka_topic, raw_event)
                print(f"finished {filename}. sent to kafka Topic: {self.config.kafka_topic}")