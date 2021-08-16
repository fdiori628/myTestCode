from Common.yaml_until import YamlUtil


class ReadConfig:

    def __init__(self, file_path, **kwargs):
        self._readfile = YamlUtil(file_path).read_yaml()
        self._writefile = YamlUtil(file_path, **kwargs).write_yaml

    def read_file(self):
        return self._readfile

    def write_file(self):
        self._writefile()
        print('write file successufl')
