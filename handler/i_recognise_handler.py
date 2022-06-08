from dto.request_dto import RequestDTO


class IRecogniseHandler:

    def subscribe(self, topic_name: str):
        pass

    def get_request(self) -> RequestDTO:
        pass
