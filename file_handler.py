import re
import json

def get_data(path,key) :
    result = []
    dataset = open(path)
    for current_data in dataset:
        json_review = json.loads(current_data)
        result.append(json_review[key])
    return result

def get_data_2(path):
    result = {}
    dataset = open(path)
    for data in dataset :
        split = re.findall('\'title\': \'.*?(?=\')\'', data)
        value = str(split)[12:-3]
        split = re.findall('{\'asin\': \'.*?(?=\')\'', data)
        key = str(split)[12:-3]
        result[key] = value
    return result