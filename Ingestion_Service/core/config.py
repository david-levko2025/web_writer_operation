from typing import Dict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    FOLDER_PATH : str = r"C:\Users\DELL\web_writer_operation\tweet_images"
    FASTAPI_URL : str= "http://127.0.0.1:8000/metadata"
    KAFKA_CONFIG : Dict[str,str] = {'bootstrap.servers': 'localhost:9092'} 
    TOPIC_NAME : str= 'tweet_data'

settings = Settings()