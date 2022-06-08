from dto.image_dto import ImageDTO


class RequestDTO:
    def __init__(self, image_dto: ImageDTO, date):
        self.image_dto = image_dto
        self.date = date

    def get_image_dto(self):
        return self.image_dto

    def get_date(self):
        return self.date

    def set_image_dto(self, image_dto):
        self.image_dto = image_dto

    def set_date(self, date):
        self.date = date

    def __str__(self):
        return f'RequestDTO(date={self.get_date()}, image_dto={self.get_image_dto()})'
