import json

from confluent_kafka import Consumer

from dto.image_dto import ImageDTO
from dto.request_dto import RequestDTO
from handler.i_recognise_handler import IRecogniseHandler


class RecogniseHandler(IRecogniseHandler):
    def __init__(self, options_path):
        self.options = self.parse_config(options_path)
        self.consumer = Consumer(self.options)

    # преобразует данные из документа в словарь
    def parse_config(self, options_path):
        with open(options_path, 'r') as options:
            dict_options = json.load(options)
        return dict_options

    # создаем consumer и подписываемся на топик
    def subscribe(self, topic):
        self.consumer.subscribe([topic])

    # возвращает декодированные сообщения, полученные из топика
    # def trace_response(self, msg):
    #     msg_str = msg.value().decode('utf-8')
    #     print('Consumed message from topic {} partition: [{}] at offset {}:'.format(msg.topic(), msg.partition(),
    #                                                                                 msg.offset()))
    #     # print('key: {}, value: {}'.format(str(msg.key()), self.msg_str))
    #     print(self.parse_msg(msg_str))
    #     # return self.msg_str

    # читает данные
    def get_request(self) -> RequestDTO:
        flag = True
        while flag:
            msg = self.consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                if ("PARTITION_EOF" in msg.error()):
                    flag = False
                continue

            return self.parse_msg(msg)

    #TODO передать дату
    def parse_msg(self, msg):
        msg_str = msg.value().decode('utf-8')
        data = json.loads(msg_str)
        image_dto = ImageDTO(data["Image_ID"], data["Image_Base64"])
        request_dto = RequestDTO(image_dto, None)
        return request_dto
