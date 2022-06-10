import torch

from dto.bbox_dto import BBoxDTO
from dto.i_model import IModel
from dto.request_dto import RequestDTO
from dto.response_dto import ResponseDTO
from mapper.product_id_mapper import ProductIdMapper
from mapper.request_mapper import RequestMapper
from publisher import Publisher
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

        # path = 'C:\\Users\\user\Documents\kgu\diploma\yolov5x_640_600_augment\weights\\best.pt'
        model = torch.hub.load('ultralytics/yolov5', 'custom',
                               path=self.model_dto.get_model_path())

        map_request = RequestMapper()  # создается сущность в бд
        #img = map_request.decode_imgbase64(request_dto)
        img = 'C:\\Users\\user\Desktop\photo.jpeg'
        # Inference
        results = model(img).pandas().xyxy[0].to_dict()
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

        bbox = BBoxDTO(bbox_list)

        map_product = self.map_product_id('products.csv', product_list)

        response_dto = ResponseDTO(image_id=request_dto.get_image_dto().get_id_img(), products=map_product, bbox=bbox,
                                   probability=probability_list)
        publisher = Publisher('options_producer.json')

        publisher.publish_event("response", response_dto.to_json())