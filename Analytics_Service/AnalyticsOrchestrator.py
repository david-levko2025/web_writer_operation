from KafkaConsumer import KafkaConsumer
from KafkaPublisher import KafkaPublisher
from TextAnalyzer import TextAnalyzer

consumer = KafkaConsumer()
publisher = KafkaPublisher()
textanalyzer = TextAnalyzer()

while True:
    try:
        msg = consumer.get_data_from_producer()
        if not msg :
            continue
        else:
            text = msg['clen_text']
            analyze_text_res = textanalyzer.analyze_text(text)
            count_weapon = textanalyzer.count_weapons_in_text(text)
            top_common = textanalyzer.top_10_common(text)
            data = {
                "image_id" : msg['image_id'],
                'analyze text' : analyze_text_res,
                'count weapon in text': count_weapon,
                'top 10 common' :top_common
            }

            publisher.publish_raw_event(data=data)
    except Exception as err:
        print(f'Error {err}')
