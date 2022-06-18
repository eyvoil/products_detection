from dto.model_dto import ModelDTO
from entity.model import Model
from mapper.i_mapper import IMapper


class ModelMapper(IMapper):
    def __init__(self, dto: ModelDTO):
        self.dto = dto

    def map_to_entity(self):
        model = Model(name=self.dto.get_name(), path=self.dto.get_model_path())
        return model