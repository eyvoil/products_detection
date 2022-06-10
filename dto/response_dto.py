import datetime
import json

from dto.bbox_dto import BBoxDTO


class ResponseDTO:
    def __init__(self, image_id, products, bbox: BBoxDTO, probability):
        self.image_id = image_id
        self.products = products
        self.bbox = bbox
        self.probability = probability
        self.date = datetime.datetime.now()

    def get_image_id(self):
        return self.image_id

    def get_products(self):
        return self.products

    def get_bbox(self):
        return self.bbox

    def get_probability(self):
        return self.probability

    def get_date(self):
        return self.date

    def set_image_id(self, image_id):
        self.image_id = image_id

    def set_products(self, products):
        self.products = products

    def set_bbox(self, bbox: BBoxDTO):
        self.bbox = bbox

    def set_probability(self, probability):
        self.probability = probability

    def to_json(self):
        response_dict = {"Image_ID": self.get_image_id()}
        list = []
        for i in range(len(self.get_products())):
            dict_products = {"Product_ID": self.get_products()[i],
                             "Product_frame": {
                                 "Top_Left_Corner_Coord_X": self.get_bbox().get_bbox()[i][0],
                                 "Top_Left_Corner_Coord_Y": self.get_bbox().get_bbox()[i][1],
                                 "Frame_Height": self.get_bbox().get_bbox()[i][3],
                                 "Frame_Width":  self.get_bbox().get_bbox()[i][2]
                             },
                             "Probability_recognition": self.get_probability()[i]
                            }
            list.append(dict_products)

        response_dict["Products"] = list
        response_json = json.dumps(response_dict)
        return response_json

    def __str__(self):
        return f'ResponseDTO(date={self.get_date()}, image_id={self.get_image_id()}, products={self.get_products()}, ' \
               f'bbox={self.get_bbox()}, probability={self.get_probability()}) '
