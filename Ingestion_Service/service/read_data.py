import easyocr
import os
import requests
from confluent_kafka import Producer
from PIL import Image  

from core.config import settings
from model.schema import ImageMetadata, ImageProcessResult


reader = easyocr.Reader(['en'], gpu=True)
producer = Producer(settings.KAFKA_CONFIG)  # type: ignore

def delivery_report(err, msg):

    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def process_images():

    if not os.path.exists(settings.FOLDER_PATH):
        print(f"Error: Folder {settings.FOLDER_PATH} not found.")
        return

    for filename in os.listdir(settings.FOLDER_PATH):
        if filename.lower().endswith('.png'):
            file_path = os.path.join(settings.FOLDER_PATH, filename)
            image_id = os.fsdecode(filename)

            print(f"Processing: {filename}...")

            result = reader.readtext(file_path, detail=0)
            extracted_text = " ".join(result)  # type: ignore

            with Image.open(file_path) as img:
                width, height = img.size
                img_format = img.format

            file_stats = os.stat(file_path)

            meta = ImageMetadata(
                image_id=image_id,
                filename=filename,
                size_bytes=file_stats.st_size,
                dimensions=f"{width}x{height}",
                format=img_format or "PNG"
            )

            try:
                with open(file_path, "rb") as f:
                    files = {"file": (filename, f, f"image/{meta.format.lower()}")}
                    requests.post(f"{settings.FASTAPI_URL}/upload", files=files)
            except Exception as e:
                print(f"API Binary Upload Error: {e}")


            process_result = ImageProcessResult(
                image_id=image_id,
                text=extracted_text,
                metadata=meta
            )
            

            producer.produce(
                settings.TOPIC_NAME,
                key=image_id,  # type: ignore
                value=process_result.model_dump_json(),  # type: ignore
                callback=delivery_report
            )

            producer.poll(0)


    producer.flush()


if __name__ == "__main__":
    process_images()