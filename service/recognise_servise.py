import traceback

import torch

from dto.bbox_dto import BBoxDTO
from dto.i_model import IModel
from dto.request_dto import RequestDTO
from dto.response_dto import ResponseDTO
from entity.product import Product
from mapper.model_mapper import ModelMapper
from mapper.product_id_mapper import ProductIdMapper
from mapper.request_mapper import RequestMapper
from mapper.response_mapper import ResponseMapper
from publisher import Publisher
from repository.record_repository import RecordRepository
from service.i_recognise_service import IRecogniseService


class RecogniseService(IRecogniseService):
    def __init__(self, model_dto: IModel):
        self.model_dto = model_dto

    def map_product_id(self, path, product_list):
        map_product = []
        map = ProductIdMapper(path)
        for i in product_list:
            map_product.append(map.map_product_id(i))
        return map_product

    def recognise(self, request_dto: RequestDTO):
        stack_trace = ''
        try:
            model = torch.hub.load('ultralytics/yolov5', 'custom',
                                   path=self.model_dto.get_model_path())

            # img = map_request.decode_imgbase64(request_dto)
            img = 'C:\\Users\\user\\Downloads\\Telegram Desktop\\photo_2022-06-18_14-44-57.jpg'
            # Inference
            results = model(img).pandas().xyxy[0].to_dict()
        except Exception as e:
            print(f'Ошибка {traceback.format_exc()}')


        print(results)
        bbox_list = []
        product_list = []
        probability_list = []
        for i in range(0, len(results["xmin"])):
            width = results["xmax"][i] - results["xmin"][i]
            height = results["ymax"][i] - results["ymin"][i]
            bbox_list.append([results["xmin"][i], results["ymax"][i], width, height])
            product_list.append(results["class"][i])
            probability_list.append(results["confidence"][i])

        bbox_dto = BBoxDTO(bbox_list)

        map_product = self.map_product_id('products.csv', product_list)

        response_dto = ResponseDTO(image_id=request_dto.get_image_dto().get_id_img(), products=map_product,
                                   bbox=bbox_dto, probability=probability_list)
        print(response_dto.to_json())

        request_map = RequestMapper(request_dto)
        request = request_map.map_to_entity()

        model_map = ModelMapper(self.model_dto)
        model_entity = model_map.map_to_entity()

        repository = RecordRepository()
        repository.create_logs(request, response_dto, model_entity, map_product, probability_list, bbox_dto)

        publisher = Publisher('options_producer.json')

        publisher.publish_event("response", response_dto.to_json())
