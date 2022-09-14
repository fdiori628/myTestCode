import yaml


class YamlUtil:

    def __init__(self, path):
        self._path = path
        # self._data = kwargs
        # self._Logger = Logger()

    def read_yaml(self):
        filepath = self._path
        try:
            with open(filepath, 'r') as f:
                value = yaml.load(f, Loader=yaml.FullLoader)
                # self._Logger.logger(f'file context is {value}')
                return value
        except FileExistsError as e:
            # self._Logger.logger_error(e)
            return None

    def rewrite_yaml(self, data):
        filepath = self._path
        # file_key = list(self._data.keys())[0]
        try:
            with open(filepath, 'w') as f:
                yaml.dump(data=data, stream=f, sort_keys=False)
        except FileExistsError as e:
            # self._Logger.logger_error(e)
            raise e

    def write_yaml(self, data):
        filepath = self._path
        # file_key = list(self._data.keys())[0]
        try:
            with open(filepath, 'a') as f:
                yaml.dump(data=data, stream=f, sort_keys=False)
        except FileExistsError as e:
            # self._Logger.logger_error(e)
            raise e

    def read_single_yml_name(self, name):
        try:
            with open(self._path, 'r') as f:
                value = yaml.load(f, Loader=yaml.FullLoader)
                key = self.find_disc(value, name)
        except FileExistsError as e:
            # self._Logger.logger_error(e)
            raise e
        return key[0]

    def find_disc(self, will_find_dist, find_keys):  # will_find_dist要查找的字典，find_keys要查找的keys，found找到值存放处
        value_found = []
        if isinstance(will_find_dist, (list)):  # 含有列表的值处理
            if len(will_find_dist) > 0:
                for now_dist in will_find_dist:
                    found = self.find_disc(now_dist, find_keys)
                    if found:
                        value_found.extend(found)
                return value_found

        if not isinstance(will_find_dist, dict):  # 没有字典类型的了
            return 0

        else:  # 查找下一层
            dict_key = will_find_dist.keys()
            # print (dict_key)
            for i in dict_key:
                if (i == find_keys):
                    value_found.append(will_find_dist[i])
                found = self.find_disc(will_find_dist[i], find_keys)
                if (found):
                    value_found.extend(found)

            return value_found
