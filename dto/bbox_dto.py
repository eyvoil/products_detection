class BBoxDTO:
    def __init__(self, bbox):
        self.bbox = bbox

    def get_bbox(self):
        return self.bbox

    def set_bbox(self, bbox):
        self.bbox = bbox

    def __str__(self):
        return f'BBoxDTO(bbox = {self.get_bbox()})'
