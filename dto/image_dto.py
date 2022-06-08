import base64


class ImageDTO:
    def __init__(self, id_img, img_base64):
        self.id_img = id_img
        self.img_base64 = img_base64

    def get_id_img(self):
        return self.id_img

    def get_img_base64(self):
        return self.img_base64

    def __str__(self):
        return f'ImageDTO(id_img={self.get_id_img()}, img_base64={self.get_img_base64()})'