import base64
import os

from dto.request_dto import RequestDTO
from entity.request import Request
from mapper.i_mapper import IMapper


class RequestMapper(IMapper):
    def __init__(self, dto: RequestDTO):
        self.dto = dto

    def map_to_entity(self):

        request = Request(id=self.dto.get_image_dto().get_id_img(), img_path=self.decode_imgbase64(), request_date=self.dto.get_date())
        return request

    def decode_imgbase64(self):

        msg_img = self.dto.get_image_dto().get_img_base64()
        list = msg_img.split(",")
        img_type = list[0][list[0].find('/')+1:list[0].find(';')]
        img_base64 = list[1]
        id_img = self.dto.get_image_dto().get_id_img()

        img = base64.b64decode(img_base64)
        name_img = f'image\{id_img}.{img_type}'
        image_result = open(name_img, 'wb')
        image_result.write(img)

        path_img = os.path.abspath(name_img)

        return path_img
