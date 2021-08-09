import yaml


class YamlUtil:

    def __init__(self, path, **kwargs):
        self.path = path
        self.data = kwargs

    def read_yaml(self):
        filepath = self.path
        try:
            with open(filepath, 'r') as f:
                value = yaml.load(f, Loader=yaml.FullLoader)
        except FileExistsError as e:
            raise e
        return value

    def write_yaml(self):
        filepath = self.path
        try:
            with open(filepath, 'w') as f:
                yaml.dump(data=self.data, stream=f, sort_keys=False)
        except Exception as e:
            raise (type(e), e)
