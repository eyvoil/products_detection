from confluent_kafka import Producer
import json

from i_publisher import IPublisher


class Publisher(IPublisher):
    def __init__(self, options_path):
        self.options = self.parse_option(options_path)
        self.producer = Producer(self.options)

    # преобразует данные из документа в словарь
    def parse_option(self, options_path):
        with open(options_path, 'r') as options:
            dict_options = json.load(options)
        return dict_options

    def delivery_report(self, err, msg):
        if err is not None:
            print('[ERROR] Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    def publish_event(self, topic, event: json, key=1):
        self.producer.produce(topic, key=event[key], value=event.encode('utf-8'),
                              callback=self.delivery_report)
        self.producer.flush()
