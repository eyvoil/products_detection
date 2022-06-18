import time

from sqlalchemy.exc import SQLAlchemyError

from dto.bbox_dto import BBoxDTO
from dto.model_dto import ModelDTO
from dto.response_dto import ResponseDTO
from entity.bbox import BBox
from entity.model import Model
from entity.product import Product
from entity.record import Record
from entity.request import Request
from entity.response import Response
from mapper.response_mapper import ResponseMapper
from repository.i_record_repository import IRecordRepository
from database.connect import session


class RecordRepository(IRecordRepository):
    def __init__(self):
        pass

    def create(self, obj):
        try:
            session.add(obj)  # добавляем объект
            session.commit()  # коммитим изменения
            print(f"Created: {obj}")
            return obj
        except SQLAlchemyError as e:
            print(f"Unexpected error when creating user: {e}")
            raise e

    def update(self, obj):
        pass

    def delete(self, obj):
        try:
            session.delete(obj)  # удаляем объект
            session.commit()  # коммитим изменения
            print(f"Deleted: {obj}")
        except SQLAlchemyError as e:
            print(f"Unexpected error when deleting user: {e}")
            raise e

    def find(self, obj, id):
        return obj.query.filter_by(id=id).first()

    def all(self, obj):
        return obj.query.order_by(obj.id).all()

    def create_logs(self, request: Request, response_dto: ResponseDTO, model: Model, product_list: list,
                    probability: list,
                    bbox_dto: BBoxDTO):
        self.create(request)
        self.create(model)
        print(product_list)
        product_db = []
        for i in range(len(bbox_dto.get_bbox())):
            bbox = BBox(bbox=bbox_dto.get_bbox()[i])
            self.create(bbox)
            print(bbox.id)
            product = Product(product=product_list[i], probability=probability[i], id_bbox=bbox.id)
            self.create(product)
            product_db.append(product)

        response_map = ResponseMapper(response_dto)
        response = response_map.map_to_entity()
        self.create(response)
        response.id_product = product_db
        session.commit()

        record = Record(id_request=request.id, id_response=response.id, id_model=model.id, stack_trace=None)
        self.create(record)
