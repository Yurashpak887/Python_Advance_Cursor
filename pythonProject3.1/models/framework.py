from abc import ABC
import json
class Model(ABC):
    @classmethod
    def get_data(cls, path):
        file = open('database/' + path)
        reading_file = file.read()
        data = json.loads(reading_file)
        file.close()
        return data

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_data(cls.path)
        for el in data:
            if el['id'] == id:
                print(el['name'])
                return
        print('Element not found')