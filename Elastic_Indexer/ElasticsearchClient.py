from elasticsearch import Elasticsearch

from IndexerConfig import config

class ElasticsearchClient:

    def __init__(self):
        self.client = Elasticsearch(config.elasticsearch_server)
        self.index = "images"
        self.create_schema()

    def create_schema(self):
        if not self.client.indices.exists(index=self.index):
            mapping = {
                "mappings": {
                    "properties": {
                        "image_id":                 {"type": "keyword"},
                        "text":                     {"type": "text"},
                        "image_format":             {"type": "keyword"},
                        "width":                    {"type": "integer"},
                        "height":                   {"type": "integer"},
                        "channels":                 {"type": "integer"},
                        "clean_text":               {"type": "text"},
                        "analyze_text":             {"type": "keyword"},
                        "list_of_weapons ":         {"type": "keyword"},
                        "top_common_words":         {"type": "keyword"},
                    }
                }
            }
            self.client.indices.create(index=self.index,body=mapping)

    def insert_to_elastic(self, metadata):
        self.client.update(
            index = self.index,
            id = metadata["image_id"],
            body = {"doc" : metadata, "doc_as_upsert": True},
    )