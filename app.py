from flask import Flask

from dto.request_dto import RequestDTO
from handler.i_recognise_handler import IRecogniseHandler
from handler.recognise_handler import RecogniseHandler
from publisher import Publisher
from service.i_recognise_service import IRecogniseService
from service.recognise_servise import RecogniseService

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

if __name__ == '__main__':

    handler: IRecogniseHandler = RecogniseHandler("D:\python-projects\ProductsDetection\options.json")
    handler.subscribe("purchases")

    image = open('C:\\Users\\user\\Documents\\kgu\\diploma\\milk_products\\train\\IMG_20220421_173734.jpg', 'rb')
    image_read = image.read()
    image_64_encode = "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"


    producer = Publisher("D:\python-projects\ProductsDetection\options_producer.json")
    producer.prepare_producer()
    event = {
        "_id": "12b1b2-b134h45",
        "Image_Base64": image_64_encode
    }

    producer.publish_event("purchases", event, '_id')

    recognise_service: IRecogniseService = RecogniseService()
    recognise_service.recognise(handler.get_request())


    # PRODUSER
    # producer = Producer({'bootstrap.servers':'localhost:29092'})
    #
    # # Optional per-message delivery callback (triggered by poll() or flush())
    # # when a message has been successfully delivered or permanently
    # # failed delivery (after retries).
    # def delivery_callback(err, msg):
    #     if err:
    #         print('ERROR: Message failed delivery: {}'.format(err))
    #     else:
    #         print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
    #             topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
    #
    #
    # # Produce data by selecting random values from these lists.
    # topic = "purchases"
    # user_ids = ['eabara', 'jsmith', 'sgarcia', 'jbernard', 'htanaka', 'awalther']
    # products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries']
    #
    # count = 0
    # for _ in range(1):
    #     user_id = choice(user_ids)
    #     product = choice(products)
    #     producer.produce(topic, product, user_id, callback=delivery_callback)
    #     count += 1
    # producer.flush()

    # КОННЕКТ К БД
    # new_model = Model(name = 'name', path = 'nnnnn')
    # session.add(new_model)
    # session.commit()
    # s = select(Model)
    # result = engine.connect().execute(s)
    # for row in result:
    #     print(row)
    # print(s)

    # CONSUMER
    # # Create Consumer instance
    # consumer = Consumer({'bootstrap.servers': 'localhost:29092',
    #                      'group.id': 'first_group',
    #                      'auto.offset.reset': 'earliest'})
    #
    # # Subscribe to topic
    # topic = "purchases"
    # consumer.subscribe([topic])
    #
    # # Poll for new messages from Kafka and print them.
    # try:
    #     while True:
    #         msg = consumer.poll(1.0)
    #         if msg is None:
    #             # Initial message consumption may take up to
    #             # `session.timeout.ms` for the consumer group to
    #             # rebalance and start consuming
    #             print("Waiting...")
    #         elif msg.error():
    #             print("ERROR: %s".format(msg.error()))
    #         else:
    #             # Extract the (optional) key and value, and print.
    #
    #             print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
    #                 topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
    # except KeyboardInterrupt:
    #     pass
    # finally:
    #     # Leave group and commit final offsets
    #     consumer.close()

    app.run(debug=True, port=5004)