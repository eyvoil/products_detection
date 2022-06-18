from dto.model_dto import ModelDTO
from dto.response_dto import ResponseDTO
from entity.model import Model
from entity.response import Response
from mapper.i_mapper import IMapper


class ResponseMapper(IMapper):
    def __init__(self, response_dto: ResponseDTO):
        self.response_dto = response_dto

    #TODO дописать
    def map_to_entity(self):
        response = Response(response_date=self.response_dto.get_date())

        return response

