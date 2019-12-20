import yaml
import json


with open('./sample01.yaml') as file:
    yml = yaml.load(file, Loader=yaml.FullLoader)
    print(json.dumps(yml['development']))
