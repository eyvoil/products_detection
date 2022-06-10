from dto.model_dto import ModelDTO
from dto.response_dto import ResponseDTO
from entity.model import Model
from entity.response import Response
from mapper.i_mapper import IMapper


class ResponseMapper(IMapper):
    def __init__(self):
        pass
    #TODO дописать
    def map_to_entity(self, response_dto: ResponseDTO):
        response = Response(response_date=response_dto.get_date())
        # model = Model(name=model_dto.get_name() , path=model_dto.get_model_path())

        return response

