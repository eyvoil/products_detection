from dto.i_model import IModel


class ModelDTO(IModel):
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path

    def get_name(self):
        return self.name

    def get_model_path(self):
        return self.path

    def set_name(self, name):
        self.name = name

    def set_path(self, path):
        self.path = path

    def __str__(self):
        return f'ModelDTO(name={self.get_name()}, path={self.get_model_path()})'
