import json

from kafka_consumer import KafkaConsumer
from kafka_publisher import KafkaPublisher
from text_cleaner import TextCleaner

consumer = KafkaConsumer()
publisher = KafkaPublisher()
clean_text = TextCleaner()

while True:
    try:
        msg = consumer.get_data_from_producer()
        if not msg:
            continue
        else:
            text = msg['text']
            remove_stop_words = " ".join(clean_text.remove_stop_words(text))
            data = json.dumps({"image_id" : msg['image_id'],"clean_text":remove_stop_words})
            publisher.produce_data(data=data)
    except Exception as err:
        print(f"Error : {err}")