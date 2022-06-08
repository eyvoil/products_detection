from confluent_kafka import Producer
import json


class Publisher:
    def __init__(self, options_path):
        self.options = self.parse_option(options_path)

    # преобразует данные из документа в словарь
    def parse_option(self, options_path):
        with open(options_path, 'r') as options:
            dict_options = json.load(options)
        return dict_options

    # Создание Producer
    def prepare_producer(self):
        self.producer = Producer(self.options)

    def delivery_report(self, err, msg):
        if err is not None:
            print('[ERROR] Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    def publish_event(self, topic, event, key):
        data_json = json.dumps(event)
        self.producer.produce(topic, key=event[key], value=data_json.encode('utf-8'),
                              callback=self.delivery_report)
        self.producer.flush()