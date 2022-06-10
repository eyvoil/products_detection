import csv

# TODO переписать когда будут ид
class ProductIdMapper:
    def __init__(self, path):
        self.path = path

    def map_product_id(self, id_product: int):
        with open(self.path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["id"] == str(id_product):
                    return row["id_product"]