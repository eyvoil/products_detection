from dto.request_dto import RequestDTO
from service.i_recognise_service import IRecogniseService


class RecogniseService(IRecogniseService):

    def recognise(self, request_dto: RequestDTO):
        print(request_dto)
