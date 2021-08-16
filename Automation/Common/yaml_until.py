import yaml
# from Common.logger_until import Logger


class YamlUtil:

    def __init__(self, path, **kwargs):
        self._path = path
        self._data = kwargs
        # self._Logger = Logger()

    def read_yaml(self):
        filepath = self._path
        try:
            with open(filepath, 'r') as f:
                value = yaml.load(f, Loader=yaml.FullLoader)
                # self._Logger.logger(f'file context is {value}')
        except FileExistsError as e:
            # self._Logger.logger_error(e)
            raise e
        return value

    def write_yaml(self):
        filepath = self._path
        file_key = list(self._data.keys())[0]
        try:
            with open(filepath, 'w') as f:
                yaml.dump(data=self._data[file_key], stream=f, sort_keys=False)
        except FileExistsError as e:
            # self._Logger.logger_error(e)
            raise e
