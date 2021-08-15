import logging.config
from Common.yaml_until import YamlUtil
from string import Template
import time


t = time.strftime('%Y%m%d')
dict_conf = YamlUtil('../../Config.yaml').read_yaml()
o = dict_conf[2]['Logger']
r = dict_conf[2]['Logger']['handlers']['fileHandler']['filename']
temp = Template(r)
loggername = {
    "loggername": 'logger'
}
re = temp.substitute(loggername) + '_' + t
o['handlers']['fileHandler']['filename'] = re
print(o)

# logging.config.dictConfig(dict_conf[2]['Logger'])


# logger = logging.getLogger('applog')
# d = {
#     "name": 'Karl',
#     "age": 111
# }
#
# logger.info(f'the request body is {d}')
