from Common.yaml_until import YamlUtil
import pprint
import requests

# r = YamlUtil('myfile.yaml').read_yaml()
# pprint.pprint(r)

data = {
    "title": "json-server5",
    "author": "typicode5"
}

r = requests.request('post', 'http://localhost:3000/posts', data=data)
print(r.json())